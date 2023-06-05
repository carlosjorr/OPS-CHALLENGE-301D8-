#!/bin/bash

 Script: Ops 301 Ops Chall Class-05
# Author: carlos rojas
# Date of latest revision: 06/05/2023
# Purpose: Clearing Logs


# Define the backup directory
backup_dir="/var/log/backups"

# Create the backup directory if it doesn't exist
mkdir -p "$backup_dir"

# Get the current timestamp
timestamp=$(date +"%Y%m%d%H%M%S")

# Function to print file size
print_file_size() {
  file=$1
  size=$(du -sh "$file" | awk '{print $1}')
  echo "File size of $file: $size"
}

# Function to clear log file
clear_log_file() {
  file=$1
  : > "$file"
}

# Compress and backup log files
compress_and_backup() {
  file=$1
  compressed_file="$backup_dir/$(basename "$file")-$timestamp.zip"
  zip -r "$compressed_file" "$file" > /dev/null 2>&1
  echo "Compressed file size of $compressed_file:"
  print_file_size "$compressed_file"
}

# Print file size before compression
echo "File sizes before compression:"
print_file_size "/var/log/syslog"
print_file_size "/var/log/wtmp"

# Compress and backup log files
compress_and_backup "/var/log/syslog"
compress_and_backup "/var/log/wtmp"

# Clear log files
clear_log_file "/var/log/syslog"
clear_log_file "/var/log/wtmp"

# Print file size after compression
echo "File sizes after compression:"
print_file_size "/var/log/backups/syslog-$timestamp.zip"
print_file_size "/var/log/backups/wtmp-$timestamp.zip"

# Compare sizes
original_syslog_size=$(du -sh "/var/log/syslog" | awk '{print $1}')
compressed_syslog_size=$(du -sh "/var/log/backups/syslog-$timestamp.zip" | awk '{print $1}')

original_wtmp_size=$(du -sh "/var/log/wtmp" | awk '{print $1}')
compressed_wtmp_size=$(du -sh "/var/log/backups/wtmp-$timestamp.zip" | awk '{print $1}')

echo "Comparison of sizes:"
echo "Original syslog size: $original_syslog_size"
echo "Compressed syslog size: $compressed_syslog_size"

echo "Original wtmp size: $original_wtmp_size"
echo "Compressed wtmp size: $compressed_wtmp_size"
