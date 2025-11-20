#!/usr/bin/env python
"""
menu file for scholarship tracker
"""
from add_scholarship import add_scholarship
from view_scholarship import view_scholarships

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
        choice = input("Enter your choice:").strip()
        if choice not in ["1", "2", "3"]:
            print("Invalid choice. Enter 1, 2, or, 3")
            continue #continue goes back to the start of the while loop

        if choice == "1":
            add_scholarship()
        elif choice == "2":
            view_scholarships()
        elif choice == "3":
            print("exiting program")
            break #break ends the while loop
