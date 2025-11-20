#!/usr/bin/env python
"""
add scholarship
"""
from data import scholarships

def add_scholarship():
    """
    add scholarship menu
    """
    name = input("Scholarship name: ").strip().title()
    link = input("Scholarship link: ").strip()
    amount = input("Scholarship amount: ").strip()
    deadline = input("Scholarship deadline: ").strip()
    status = input("Scholarship status: ").strip()

    essay = input("Essay required? (y/n): ").lower().strip()
    if essay == "y":
        essay = "yes"
    if essay == "n":
        essay = "no"

    notes = input("Scholarship notes/descriptions: ").strip()

    new_scholarship = [name, link, amount, deadline, status, essay, notes]
    scholarships.append(new_scholarship)

    print("Scholarship added!")
