#!/usr/bin/env python
"""
manage scholarships
"""
import locale
from data import scholarships
from view_scholarship import view_scholarship, view_title

locale.setlocale(locale.LC_ALL, "en_US")

def manage_scholarship():
    """
    edit/delete scholarship
    """
    if not scholarships:
        print("No scholarships found.\n")
        return

    view_scholarship()
    choice = input(
        "Enter E to edit, D to delete, or M to return to main menu: "
    ).strip().upper()
    print()

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
        print("Returning to main menu.\n")
        return

def delete_scholarship():
    """
    delete scholarship
    """
    view_title()
    choice = input(
        "Enter the scholarship number to delete (or press enter to cancel): "
    ).strip()
    print()

    if not choice: #if choice is empty aka user pressed enter
        print("Delete cancelled.\n")
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
    choice = input(
        "Enter the scholarship number to edit (or press enter to cancel): "
    ).strip()
    print()

    if not choice: #if choice is empty aka user pressed enter
        print("Edit cancelled.\n")
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
    print()

    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid choice. Enter numbers 1-7.")
        return

    if choice == "1":
        scholarship[0] = input("Enter new name: ").strip().title()
        print(f"Name updated to: {scholarship[0]}\n")
    elif choice == "2":
        scholarship[1] = input("Enter new link: ").strip().lower()
        print(f"Link updated to: {scholarship[1]}\n")

    elif choice == "3":
        amount = input("Enter new amount: ").strip() #asks user for new amount (first attempt)
        while True:
            try:
                amount = float(amount.replace("$", "").replace(",", ""))
                scholarship[2] = str(f"{amount:.2f}") #stores amount with 2 decimal places in list
                formatted = locale.currency(amount, grouping=True) #format amount adding $ and ,
                print(f"Amount updated to: {formatted}\n")
                break
            except ValueError: #runs if amount couldn't be converted to float
                amount = input("Invalid amount. Enter a number: ").strip() #asks user again
                #then goes back to top of while loop

    elif choice == "4":
        scholarship[3] = input("Enter new deadline (MM/DD/YYYY): ").strip()
        print(f"Deadline updated to: {scholarship[3]}\n")

    elif choice == "5":
        scholarship[4] = input(
            "Enter status (incomplete/ongoing/complete): "
        ).strip().lower()
        while scholarship[4] not in ["incomplete", "ongoing", "complete"]:
            scholarship[4] = input("Enter incomplete, ongoing, or complete: ").strip().lower()

        print(f"Status updated to: {scholarship[4]}\n")

    elif choice == "6":
        essay = input("Essay required? (y/n): ").strip().lower()
        while essay not in ["y", "n"]:
            essay = input("Invalid response. Enter y or n: ").strip().lower()
        if essay == "y":
            scholarship[5] = "yes"
        elif essay == "n":
            scholarship[5] = "no"

        print(f"Essay required updated to: {scholarship[5]}\n")

    elif choice == "7":
        scholarship[6] = input("Enter new notes: ").strip()
        print(f"New Notes: {scholarship[6]}\n")
