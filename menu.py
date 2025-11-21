#!/usr/bin/env python
"""
menu file for scholarship tracker
"""
from add_scholarship import add_scholarship
from manage_scholarship import manage_scholarship

def display_main_menu():
    """
    displays main menu
    """
    print("Main Menu")
    print("1. Add Scholarship")
    print("2. View/Edit Scholarships")
    print("3. Save and Exit Program")

def main_menu():
    """
    main menu that gives user to add, view/edit scholarships, or exit program"""
    while True:
        display_main_menu()
        choice = input("Enter your choice: ").strip()
        print()
        if choice not in ["1", "2", "3"]:
            print("Invalid choice. Enter 1, 2, or, 3.\n")
            continue #continue goes back to the start of the while loop

        if choice == "1":
            add_scholarship()
        elif choice == "2":
            manage_scholarship()
        elif choice == "3":
            print("Saving and exiting program...")
            break #break ends the while loop
