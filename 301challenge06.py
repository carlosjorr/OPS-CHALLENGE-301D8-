#!/usr/bin/env python3


#Script:                       Ops 301 Ops Chall 06
# Author:                       carlos rojas 
# Date of latest revision:      06/06/2023
# Purpose:                      bash im python





import os

# Declare and initialize variables
name = "John"  # Variable storing a string value
age = 25  # Variable storing an integer value
city = "New York"  # Variable storing a string value

# Print variable values
print("Name:", name)
print("Age:", age)
print("City:", city)

# Execute bash commands using os.system()
os.system("whoami")  # Execute 'whoami' command
os.system("ip a")  # Execute 'ip a' command
os.system("lshw -short")  # Execute 'lshw -short' command

