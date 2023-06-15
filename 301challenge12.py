#!/usr/bin/env python3

#Script:                       Ops 301 Ops Chall 12
# Author:                       carlos rojas 
# Date of latest revision:      06/14/2023
# Purpose:                       Python Requests Library




import requests

# Prompt the user for the destination URL
url = input("Enter the destination URL: ")

# Prompt the user to select an HTTP method
http_method = input("Select an HTTP method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ")

# Print the request information
print(f"Sending {http_method} request to {url}")

# Ask for user confirmation
confirmation = input("Proceed with the request? (Y/N): ")

if confirmation.lower() == "y":
    # Perform the request
    response = requests.request(http_method, url)

    # Print the response headers
    print("\nResponse headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")

    # Translate status code to plain terms
    status_code = response.status_code
    if status_code == 200:
        print("Request successful")
    elif status_code == 404:
        print("Site not found")
    elif status_code == 500:
        print("Internal server error")
    # Add more status code translations as needed

    # Print the response content
    print("\nResponse content:")
    print(response.text)
else:
    print("Request canceled by the user.")
