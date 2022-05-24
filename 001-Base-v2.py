"""This is my Base for my Comparison Project.
This will hold my plans for the project.
Each component will be made in it's own file
and when completed added into this one.
This has my first component which asks user for budget
Made by Daniel Fraser
8/5/22"""

# Import statements


# Functions
# Function to check for blank answer
def blank_check(ask_value):
    while True:
        response = input(ask_value).title()
        if not response:    # Checks if name has at least 1 letter
            print("***Please do not leave this blank!***")    # Error message
        else:
            return response    # Returns name


# Function to check for variables
def int_check(question):
    number = ""
    while not number:
        # Asking for a number and checking if it is valid
        try:
            number = float(blank_check(question))
            if number <= 0:  # Checking for negative number
                print("\nPlease enter an amount above 0")
                number = 0  # Resets number to 0
            else:
                return number
        except ValueError:
            print("\nPlease enter a number (Does not have to be whole)")


# Function that asks for the item's information


# Function for finding out which item is the best for its amount


# Function for working out which is the best option based on budget

# *** Main Routine ***
# Lists to hold data

# Variables and constants

# Introduction and instructions

# Ask for user's budget
budget = int_check("What is your budget? >> $")
print(f"Your budget is ${budget:,.2f}")

# Beginning the item information loop
