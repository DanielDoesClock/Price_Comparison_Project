"""This is v2 of the first component of my Price Comparison Project
It will ask the user what the maximum amount they want to spend on their items
And I have added an integer checker
Made by Daniel Fraser
5/5/22"""


def budget_check(question):
    number = ""
    while not number:
        # Asking for a number and checking if it is valid
        try:
            number = float(input(question))
            return number
        except ValueError:
            print("\nPlease enter a number for your budget")


budget = budget_check("What is your budget? >> ")
print(budget)
