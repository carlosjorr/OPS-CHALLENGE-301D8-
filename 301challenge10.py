#!/usr/bin/env python3

#Script:                       Ops 301 Ops Chall 10
# Author:                       carlos rojas 
# Date of latest revision:      06/12/2023
# Purpose:                        File Handling


# Creating a new .txt file and appending three lines
file_path = "example.txt"

with open(file_path, "w") as file:
    file.write("today its a great day\n")
    file.write("Second line\n")
    file.write("Third line\n")

# Reading and printing the first line
with open(file_path, "r") as file:
    first_line = file.readline()
    print("First line:", first_line)

# Deleting the .txt file
import os

if os.path.exists(file_path):
    os.remove(file_path)
    print("File deleted successfully.")
else:
    print("File does not exist.")
