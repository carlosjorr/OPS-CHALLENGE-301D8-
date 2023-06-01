#!/bin/bash
# autor           carlos rojas 
# Script:         Ops 301 Ops Chall 02
# Purpose:        Append, date and time
# Why:            Time stamping is a critical step in automating log generation.


#!/bin/bash

# Get the current date and time
datetime=$(date +%Y%m%d%H%M%S)

# Set the source and destination filenames
source_file="/var/log/syslog"
destination_file="syslog_${datetime}.log"

# Copy the source file to the destination
cp "$source_file" "$destination_file"

# Check if the copy was successful
if [ $? -eq 0 ]; then
    echo "File copied successfully to $destination_file"
else
    echo "Error: Failed to copy file"
fi
