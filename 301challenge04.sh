#!/bin/bash

#Script:                       Ops 301 Ops Chall 03
# Author:                       carlos rojas 
# Date of latest revision:      06/01/2023
# Purpose:                      bash script that launches a menu system

#!/bin/bash

while true; do
    # Display the menu options
    echo "Menu:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"
    read -p "Enter your choice (1-4): " choice
    echo

    # Use a conditional statement to evaluate the user's input
    case $choice in
        1)
            echo "Hello world!"
            ;;
        2)
            ping -c 127.0.0.1
            ;;
        3)
            ip a
            ;;
        4)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid choice. Please enter a number from 1 to 4."
            ;;
    esac

    echo
done
