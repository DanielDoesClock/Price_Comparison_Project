"""This is v3 of the first component of my Price Comparison Project
In this version i will be making the function more versatile
Made by Daniel Fraser
5/5/22"""

number_not_neg = 0


def int_check(question):
    number = ""
    while not number:
        # Asking for a number and checking if it is valid
        try:
            number = float(input(question))
            if number > 0:
                return number
            else:
                print(number)
                number_not_neg == number
                print(number_not_neg)
                number += number
                print(number)
                number += number_not_neg
                return number
        except ValueError:
            print("\nPlease enter a number (Does not have to be whole)")


budget = int_check("What is your budget? >> ")
print(budget)
