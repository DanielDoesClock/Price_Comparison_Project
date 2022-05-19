"""This is v2 of the first component of my Price Comparison Project
It will ask the user what the maximum amount they want to spend on their items
And I have added an integer checker
Made by Daniel Fraser
5/5/22"""


def budget_check(question):
    budget2 = ""
    while not budget2:
        # Asking for a number and checking if it is valid
        try:
            budget2 = float(input(question))
            return budget2
        except ValueError:
            print("\nPlease enter a number for your budget")


budget = budget_check("What is your budget? >> ")
print(budget)
