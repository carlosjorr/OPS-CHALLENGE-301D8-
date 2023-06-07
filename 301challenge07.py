
#!/usr/bin/env python3

#Script:                       Ops 301 Ops Chall 07
# Author:                       carlos rojas 
# Date of latest revision:      06/07/2023
# Purpose:                       Directory Creation


import os

def generate_directory_structure(directory_path):
    # Traverse the directory tree rooted at the provided path
    for root, dirs, files in os.walk(directory_path):
        level = root.replace(directory_path, '').count(os.sep)  # Calculate the depth level
        indent = ' ' * 4 * level  # Set the indentation based on the depth level
        print('{}{}/'.format(indent, os.path.basename(root)))  # Print the current directory

        sub_indent = ' ' * 4 * (level + 1)  # Increase indentation for subdirectories and files
        for file in files:
            print('{}{}'.format(sub_indent, file))  # Print the files within the current directory

# Prompt the user to enter a directory path
user_path = input("Enter the directory path: ")

# Generate and print the directory structure for the provided path
generate_directory_structure(user_path)
