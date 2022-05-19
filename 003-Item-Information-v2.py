"""This is the 2nd component of my price comparison project.
This second version will make sure the user can not input any silly values into
the questions.
Made by Daniel Fraser
13/05/22"""

item_names = []
item_prices = []
item_weights = []


def blank_check(ask_value):
    while True:
        response = input(ask_value).title()
        if not response:    # Checks if name has at least 1 letter
            print("***Please do not leave this blank!***")    # Error message
        else:
            return response    # Returns name


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


def item_info():
    more_items = blank_check("Do you want to compare an item? >> ").lower()
    # List of answers that the user could say that indicate they want to or do
    # not want to continue
    yes_ans = ["y", "yes", "yup", "ok", "sure"]
    no_ans = ["n", "no", "nope", "negative", "stop"]
    while more_items in yes_ans:
        name = blank_check("What is the name of the product? >> ")
        item_names.append(name)    # Puts into list
        price = int_check(f"What is the price of one {name}? >> ")
        item_prices.append(price)    # Puts into list
        weight = int_check(f"What is the net weight of one {name}? (In grams)"
                           f" >> ")
        item_weights.append(weight)    # Puts into list
        more_items = blank_check("Do you want to compare an item? >> ").lower()
    if more_items in no_ans:
        print("End")    # Temp end message
    else:
        print("Please answer with 'Yes' or 'No'")
        item_info()    # Loops the code


item_info()
print(item_names)
print(item_prices)
print(item_weights)
