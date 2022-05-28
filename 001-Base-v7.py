"""This is my Base for my Comparison Project.
This will hold my plans for the project.
Each component will be made in it's own file
and when completed added into this one.
Added component 5 'Ask user'
Made by Daniel Fraser
28/5/22"""

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


# Function to validate a response
def get_choice(choice, valid_choices):
    choice_error = "Sorry, that is not a valid choice"
    for list_item in valid_choices:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    print(choice_error)


# Function that asks for the item's information
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
        best_value_()  # Goes to next part of the code
    else:
        item_info()    # Loops the code


# Function for finding out which item is the best for its amount
def best_value_():
    for i in range(0, len(item_names)):
        item_worth.append(item_weights[i] / item_prices[i])
        # Made list to find the worth of the item
    if len(item_worth) < 2:
        print("There aren't enough items to compare")

    else:
        best_value = item_worth.index(max(item_worth))
        print(f"\nThe best value item is **** {item_names[best_value]} ****\n")


# Function for working out which is the best option based on budget
def best_buy_():
    best_value = item_worth.index(max(item_worth))
    best_value_name = item_names[best_value]
    if item_worth[best_value] > budget:
        # Checks for if the best value item is within budget
        print(f"But your budget is ${budget} and a {best_value_name} is "
              f"${item_prices[best_value]}")
        for i in [item_worth, item_prices, item_names, item_weights]:
            try:
                i.remove(i[best_value])
            except ValueError:
                pass
        # Removing the too expensive item
        best_value = item_worth.index(max(item_worth))
        while item_prices[best_value] > budget and len(item_prices) > 1:
            best_value = item_worth.index(max(item_worth))
            # Checking if the 2nd best item is within the budget
            for i in [item_worth, item_prices, item_names, item_weights]:
                try:
                    i.remove(i[best_value])
                except ValueError:
                    pass
            # If not, remove it and repeat
            if len(item_worth) == 1:
                best_value = 0
                best_value_name = item_names[0]
                print("\nThere are no items within your budget. \nIt would be "
                      f"best to go for * {best_value_name} * as it is the "
                      f"cheapest item at ${item_prices[best_value]}")
                # Message if no items are within budget
            else:
                best_value = item_worth.index(max(item_worth))
                best_value_name = item_names[best_value]
                print(f"\nThe best option within your budget is "
                      f"*** {best_value_name} *** at "
                      f"${item_prices[best_value]}")


# Function to ask user if they want to get the final list
def ask_user():
    show_list = blank_check("Would you like a list of all other items "
                            "listed by worth? >> ").lower()
    viable_ans = [["yes", "yup", "sure", "y"], ["no", "nope", "negative", "n"]]
    valid = get_choice(show_list, viable_ans)
    if not valid:
        print("Please enter with Y/N")
        ask_user()
    elif valid == "Yes":
        print("Continues to next part of code")  # Temp message
    else:
        print("End of program")  # Temp message


# *** Main Routine ***
# Lists to hold data
item_names = []
item_prices = []
item_weights = []
item_worth = []
sorted_list = []
# Variables and constants

# Introduction and instructions

# Ask for user's budget
budget = int_check("What is your budget? >> $")
print(f"Your budget is ${budget:,.2f}")

# Beginning the item information loop
item_info()

# Asking user if they want to see the final list
ask_user()
