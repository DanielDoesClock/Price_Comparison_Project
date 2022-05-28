"""This is the 6th component in my Price Comparison Project
This component will create a list with all item names and price
sorted by worth
Made By Daniel Fraser
27/05/22"""


def get_choice(choice, valid_choices):
    choice_error = "Sorry, that is not a valid choice"
    for list_item in valid_choices:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    print(choice_error)


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


def other_item_worth():
    show_list = input("Would you like a list of all other items "
                      "listed by worth? >> ").lower()
    viable_ans = [["yes", "yup", "sure", "y"], ["no", "nope", "negative", "n"]]
    valid = get_choice(show_list, viable_ans)
    if not valid:
        print("Please enter with Y/N")
        other_item_worth()
    elif valid == "Yes":
        sort_items()
    else:
        print("End I think")


def sort_items():
    item_num = 0
    list_length = len(item_names)
    while item_num < list_length:
        sorted_list.append([])
        sorted_list[item_num].append(item_worth[item_num])
        sorted_list[item_num].append(item_names[item_num])
        sorted_list[item_num].append(item_prices[item_num])
        item_num += 1
    print(sorted_list)


sorted_list = []
# This list assumes you are not comparing more than 5 items
item_names = []
item_prices = []
item_weights = []
item_worth = []

# Ask for user's budget
budget = int_check("What is your budget? >> $")
print(f"Your budget is ${budget:,.2f}")

# Beginning the item information loop
item_info()
other_item_worth()
