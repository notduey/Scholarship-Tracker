#!/usr/bin/env python
"""
manage scholarships
"""
from data import scholarships
from view_scholarship import view_scholarship, view_title

def manage_scholarship():
    """
    edit/delete scholarship
    """
    if not scholarships:
        print("No scholarships found.")
        return

    view_scholarship()
    choice = input("Enter D to delete, E to edit, or M to return to main menu: ").strip().upper()

    while choice not in ["D", "E", "M"]:
        print("Invalid choice. Enter D, E, or M.")
        choice = input(
            "E to edit, D to delete, or M to return to main menu: "
            ).strip().upper()

    if choice == "E":
        edit_scholarship()
    elif choice == "D":
        delete_scholarship()
    elif choice == "M":
        print("Returning to main menu.")
        return

def delete_scholarship():
    """
    delete scholarship
    """
    view_title()
    choice = input("Enter the scholarship number to delete (or press enter to cancel): ").strip()

    if not choice: #if choice is empty aka user pressed enter
        print("Delete cancelled.")
        return

    try:
        choice = int(choice)
    except ValueError as e:
        print("Invalid number. Error: ", e)
        return

    if choice < 1 or choice > len(scholarships):
        print("Number out of range.")
        return

    deleted = scholarships.pop(choice - 1) #choice - 1 because index starts at 0
    print(f"\"{deleted[0]}\" has been deleted.\n") #deleted[0] is 0th index of row
    #which is the name of the scholarship

def edit_scholarship():
    """
    edits scholarship info
    """
    view_title()
    choice = input("Enter the scholarship number to edit (or press enter to cancel): ").strip()

    if not choice: #if choice is empty aka user pressed enter
        print("Edit cancelled.")
        return

    try:
        choice = int(choice)
    except ValueError as e:
        print("Invalid number. Error: ", e)
        return

    if choice < 1 or choice > len(scholarships):
        print("Number out of range.")
        return

    scholarship = scholarships[choice -1] #choice - 1 because index starts at 0

    print("1. Name")
    print("2. Link")
    print("3. Amount")
    print("4. Deadline")
    print("5. Status")
    print("6. Essay required")
    print("7. Notes")

    choice = input(
        "Enter the number corresponding to what field you want to edit (1-7): "
        ).strip()

    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid choice. Enter numbers 1-7.")
        return

    if choice == "1":
        scholarship[0] = input("Enter new name: ").strip().title()
        print(f"Name updated to: {scholarship[0]}\n")
    elif choice == "2":
        scholarship[1] = input("Enter new link: ").strip()
        print(f"Link updated to: {scholarship[1]}\n")
    elif choice == "3":
        scholarship[2] = input("Enter new amount: ").strip()
        print(f"Amount updated to: {scholarship[2]}\n")
    elif choice == "4":
        scholarship[3] = input("Enter new deadline: ").strip()
        print(f"Deadline updated to: {scholarship[3]}\n")
    elif choice == "5":
        scholarship[4] = input("Enter status: ").strip()
        print(f"Status updated to: {scholarship[4]}\n")
    elif choice == "6":

        essay = input("Essay required? (y/n): ").strip().lower()
        if essay == "y":
            scholarship[5] = "yes"
        elif essay == "n":
            scholarship[5] = "no"
        else:
            print("Invalid choice. Enter y or n.")

        print(f"Essay required: {scholarship[5]}\n")

    elif choice == "7":
        scholarship[6] = input("Enter new notes: ").strip()
        print(f"New Notes: {scholarship[6]}\n")
