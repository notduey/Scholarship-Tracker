#!/usr/bin/env python
"""
view scholarships
"""
import locale #for currency
from data import scholarships

locale.setlocale(locale.LC_ALL, "en_US") #sets locale to en_US

def view_scholarship():
    """
    loop through scholarships
    """

    print("Scholarships:\n")

    for i, row in enumerate(scholarships, start=1):
        #enumerate() function adds a counter to the list
        #start=1 starts the counter at 1 instead of 0
        print(f"{i}. {row[0]}") #prints scholarship number and name
        print(f" Link: {row[1]}")

        amount = float(row[2]) #converts string to float
        formatted = locale.currency(amount, grouping=True) #grouping=True adds commas
        print(f" Amount: {formatted}")

        print(f" Deadline: {row[3]}")
        print(f" Status: {row[4]}")
        print(f" Essay required: {row[5]}")
        print(f" Notes: {row[6]}")
        print()

def view_title():
    """
    loop through titles
    """
    if not scholarships: #if not checks if scholarships list is empty
        print("No scholarships found.")
        return

    print("Scholarships:\n")

    for i, row in enumerate(scholarships, start=1):
        #enumerate() function adds a counter to the list
        #start=1 starts the counter at 1 instead of 0
        print(f"{i}. {row[0]}") #prints scholarship number and name
        print()
