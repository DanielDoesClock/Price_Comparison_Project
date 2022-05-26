"""This is the 2nd component of my price comparison project.
This third version will get rid of the "Do you want to continue?" part of this
code, and add a stop key.
Made by Daniel Fraser
26/05/22"""

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
    name = blank_check("What is the name of the product? >> ").title()
    if name != "X":
        item_names.append(name)    # Puts into list
    while name != "X":
        price = int_check(f"What is the price of one {name}? >> $")
        item_prices.append(price)    # Puts into list
        weight = int_check(f"What is the net weight of one {name}? (In grams)"
                           f" >> ")
        item_weights.append(weight)    # Puts into list
        name = blank_check("What is the name of the product? >> ").title()
        if name != "X":
            item_names.append(name)    # Puts into list
    if name == "X":
        print("End")    # Temp end message
    else:
        item_info()    # Loops the code


item_info()
print(item_names)
print(item_prices)
print(item_weights)
