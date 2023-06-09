#!/usr/bin/env python3

#Script:                       Ops 301 Ops Chall 09
# Author:                       carlos rojas 
# Date of latest revision:      06/09/2023
# Purpose:                       conditional statements



# Variable Declarations
age = 25
country = "USA"
income = 50000
employed = True

# Main

# if statement
if age >= 18:
    print("You are eligible to vote.")

# if-else statement
if country == "USA":
    print("You are in the United States.")
else:
    print("You are in a different country.")

# if-elif-else statement
if income >= 100000:
    print("You belong to the high-income group.")
elif income >= 50000:
    print("You belong to the middle-income group.")
else:
    print("You belong to the low-income group.")

# Nested if statement
if employed:
    print("You have a job.")
    if income >= 50000:
        print("You have a decent income.")
    else:
        print("You need to work on improving your income.")
else:
    print("You are currently unemployed.")

# Complex logical conditions
if age >= 18 and country == "USA" and (income >= 50000 or employed):
    print("You meet the criteria for various opportunities.")
else:
    print("You may have some limitations based on the conditions.")

# End
