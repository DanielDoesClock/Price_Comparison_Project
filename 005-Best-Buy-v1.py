"""This is my 4th component for my Price Comparison project.
This component will use the previous components and work out which is item is
the best for their budget.
Made By Daniel Fraser
20/05/22"""

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
    if len(item_worth) < 2:
        print("There aren't enough items to compare")

    else:
        best_value = item_worth.index(max(item_worth))
        print(f"\nThe best value item is *** {item_names[best_value]} ***\n")
    best_buy_()  # Loops to next part of code


def best_buy_():
    best_value = item_worth.index(max(item_worth))
    best_value_name = item_names[best_value]
    if item_worth[best_value] > budget:
        # Checks for if the best value item is within budget
        print(f"But your budget is ${budget} and a {best_value_name} is "
              f"${item_prices[best_value]}")
        item_names.remove(item_names[best_value])
        item_worth.remove(item_worth[best_value])
        item_weights.remove(item_weights[best_value])
        item_prices.remove(item_prices[best_value])
        # Removing the too expensive item
        best_value = item_worth.index(max(item_worth))
        while item_prices[best_value] > budget and len(item_prices) > 1:
            best_value = item_worth.index(max(item_worth))
            # Checking if the 2nd best item is within the budget
            item_names.remove(item_names[best_value])
            item_worth.remove(item_worth[best_value])
            item_weights.remove(item_weights[best_value])
            item_prices.remove(item_prices[best_value])
            # If not, remove it and repeat
            if len(item_worth) == 1:
                best_value = 0
                best_value_name = item_names[0]
                print("\nThere are no items within your budget. It would be "
                      f"best to go for * {best_value_name} * as it is the "
                      f"cheapest item at ${item_prices[best_value]}")
                # Message if no items are within budget
        best_value = item_worth.index(max(item_worth))
        best_value_name = item_names[best_value]
        print(f"\nThe best option within your budget is "
              f"*** {best_value_name} *** at ${item_prices[best_value]}")


# Main Routine
budget = int_check("What is your budget? >> $")
print(f"Your budget is ${budget:,.2f}")
item_info()

