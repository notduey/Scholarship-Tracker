#!/usr/bin/env python
"""
view/edit
"""
from data import scholarships

def view_scholarships():
    """
    view scholarships
    """
    if not scholarships:
        print("No scholarships found")
        return

    print("Scholarships:\n")

    for i, row in enumerate(scholarships, start=1):
        #enumerate() function adds a counter to the list
        #start=1 starts the counter at 1 instead of 0
        print(f"{i}.") #prints scholarship number
        print(f"Name: {row[0]}")
        print(f"Link: {row[1]}")
        print(f"Amount: {row[2]}")
        print(f"Deadline: {row[3]}")
        print(f"Status: {row[4]}")
        print(f"Essay required: {row[5]}")
        print(f"Notes: {row[6]}")
        print("\n")
