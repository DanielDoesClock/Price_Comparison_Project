"""This is v3 of the first component of my Price Comparison Project
In this version i will be making the function more versatile
Made by Daniel Fraser
5/5/22"""


def int_check(question):
    number = ""
    while not number:
        # Asking for a number and checking if it is valid
        try:
            number = float(input(question))
            if number <= 0:  # Checking for negative number
                print("\nPlease enter an amount above 0")
                number = 0  # Resets number to 0
            else:
                return number
        except ValueError:
            print("\nPlease enter a number (Does not have to be whole)")


budget = int_check("What is your budget? >> ")
print(f"Your budget is ${budget}")
