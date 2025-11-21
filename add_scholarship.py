#!/usr/bin/env python
"""
add scholarship
"""
from data import scholarships

def add_scholarship():
    """
    add scholarship with relevant information
    """
    name = input("Scholarship name: ").strip().title()
    link = input("Scholarship link: ").strip().lower()

    amount = input("Scholarship amount: ").strip()
    while True:
        try:
            #trys removing $ and ,that user might enter then converts string to float
            amount = float(amount.replace("$", "").replace(",", ""))
            break
        except ValueError:
            amount = input("Invalid amount. Enter a number:").strip()

    deadline = input("Scholarship deadline (MM/DD/YYYY): ").strip()

    status = input(
        "Scholarship status (incomplete/ongoing/complete): "
    ).strip().lower()
    while status not in ["incomplete", "ongoing","complete"]:
        status = input("Enter incomplete, ongoing, or complete: ").strip().lower()

    essay = input("Essay required? (y/n): ").strip().lower()
    while essay not in ["y", "n"]:
        essay = input("Invalid response. Enter y or n: ").strip().lower()
    if essay == "y":
        essay = "yes"
    else:
        essay = "no"

    notes = input("Scholarship notes/descriptions: ").strip()
    print()

    new_scholarship = [name, link, amount, deadline, status, essay, notes]
    scholarships.append(new_scholarship)

    print("Scholarship added!\n")
