#!/bin/bash

#Script:                       Ops 301 Ops Chall 03
# Author:                       carlos rojas 
# Date of latest revision:      06/01/2023
# Purpose:                      bash script that alters file permissions of everything in a directory. 






# Prompt user for input directory path
read -p "Enter the directory path: " directory

# Prompt user for input permissions number
read -p "Enter the permissions number (e.g., 777): " permissions

# Change directory
cd "$directory" || exit

# Change permissions of all files inside the directory
chmod -R "$permissions" *

# Print directory contents and new permissions settings
echo "Directory Contents:"
ls -l
