"""This is my 3rd component for my Price Comparison project.
This component will use component 2 to find the information of the product
and use that information to tell the user which is the best to buy based on the
net weight and the price.
Made By Daniel Fraser
19/05/22"""

item_names = []
item_prices = []
item_weights = []
item_worth = []


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
def item_info():
    more_items = blank_check("Do you want to compare an item? >> ").lower()
    # List of answers that the user could say that indicate they want to or do
    # not want to continue
    yes_ans = ["y", "yes", "yup", "ok", "sure"]
    no_ans = ["n", "no", "nope", "negative", "stop"]
    while more_items in yes_ans:
        name = blank_check("What is the name of the product? >> ")
        item_names.append(name)    # Puts into list
        price = int_check(f"What is the price of one {name}? >> $")
        item_prices.append(price)    # Puts into list
        weight = int_check(f"What is the net weight of one {name}? "
                           f"(In grams) >> ")
        item_weights.append(weight)    # Puts into list
        more_items = blank_check("Do you want to compare an item? >> ").lower()
    if more_items in no_ans:
        best_value_()   # Goes to the next part of the code
    else:
        print("Please answer with 'Yes' or 'No'")
        item_info()    # Loops the code


def best_value_():
    for i in range(0, len(item_names)):
        item_worth.append(item_weights[i] / item_prices[i])
        # Made list to find the worth of the item
    best_value = item_worth.index(max(item_worth))
    print(f"\nThe best value item is **** {item_names[best_value]} ****\n")


item_info()
