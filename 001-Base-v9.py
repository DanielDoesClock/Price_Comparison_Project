"""This is my Base for my Comparison Project.
This will hold my plans for the project.
Each component will be made in it's own file
and when completed added into this one.
Added instructions
Made by Daniel Fraser
30/5/22"""


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
        # Made list to find the worth of the item
        item_worth.append(item_weights[i] / item_prices[i])
    if len(item_worth) < 2:
        print("There aren't enough items to compare")
    else:
        best_value = item_worth.index(max(item_worth))
        print(f"\nThe best value item is **** {item_names[best_value]} ****\n")
        sort_items()
        ask_user()


# Function for working out which is the best option based on budget
def best_buy_():
    best_value = item_worth.index(max(item_worth))
    best_value_name = item_names[best_value]
    # Checks for if the best value item is within budget
    if item_worth[best_value] > budget:
        print(f"But your budget is ${budget} and a {best_value_name} is "
              f"${item_prices[best_value]}")
        # Removing the too expensive item
        for i in [item_worth, item_prices, item_names, item_weights]:
            try:
                i.remove(i[best_value])
            except ValueError:
                pass
        best_value = item_worth.index(max(item_worth))
        while item_prices[best_value] > budget and len(item_prices) > 1:
            best_value = item_worth.index(max(item_worth))
            # Checking if the 2nd best item is within the budget
            for i in [item_worth, item_prices, item_names, item_weights]:
                # If not, remove it and repeat
                try:
                    i.remove(i[best_value])
                except ValueError:
                    pass
            if len(item_worth) == 1:
                best_value = 0
                best_value_name = item_names[0]
                # Message if no items are within budget
                print("\nThere are no items within your budget. \nIt would be "
                      f"best to go for * {best_value_name} * as it is the "
                      f"cheapest item at ${item_prices[best_value]}")
                ask_user()  # Goes to next part of the program
        else:
            best_value = item_worth.index(max(item_worth))
            best_value_name = item_names[best_value]
            print(f"\nThe best option within your budget is "
                  f"*** {best_value_name} *** at "
                  f"${item_prices[best_value]}")
            ask_user()  # Goes to next part of the code


# Function to ask user if they want to get the final list
def ask_user():
    show_list_ = blank_check("Would you like a list of all other items "
                             "listed by worth? >> ").lower()
    valid_ = get_choice(show_list_, viable_ans)
    if not valid_:
        print("Please enter with Y/N")
        ask_user()  # Asks again
    elif valid == "Yes":
        worth_list()  # Goes to next part of the program
    else:
        print("End of program")  # Temp message


# Function that sorts all relevant information into a single nested list
def sort_items():
    item_num = 0
    list_length = len(item_names)
    while item_num < list_length:
        # This adds a new nested list into the list for every item
        sorted_list.append([])
        # Adding all item names, worth and prices to a nested list.
        # Weight is not relevant here
        sorted_list[item_num].append(item_worth[item_num])
        sorted_list[item_num].append(item_names[item_num])
        sorted_list[item_num].append(item_prices[item_num])
        item_num += 1
    sorted_list.sort(reverse=True)
    best_buy_()  # Goes to next part of the program


# Function to display the list of all items by their worth
def worth_list():
    print("\n*********** List of all items based on value ***********")
    print("\33[1;0;1m-- \33[1;31;1mOver budget\33[1;0;1m -- "
          "\33[1;33;1mRecommended item\33[1;0;1m -- \33[1;32;1mWithin budget"
          "\33[1;0;1m -- ")
    print(f"\33[1;0;1mBudget - ${budget}")
    item_num = 0
    # This variable is so that only 1 item is the recommended item
    stop = False
    for i in sorted_list:
        # Printing all items over the budget red
        if i[2] > budget:
            print(f"\33[1;31;1m{sorted_list[item_num][1]} - "
                  f"${sorted_list[item_num][2]}")
            item_num += 1
        # Printing the first item under the budget in gold
        elif stop is False:
            print(f"\33[1;33;1m{sorted_list[item_num][1]} - "
                  f"${sorted_list[item_num][2]}")
            stop = True
            item_num += 1
        # Printing everything else under the budget in green
        else:
            print(f"\33[1;32;1m{sorted_list[item_num][1]} - "
                  f"${sorted_list[item_num][2]}")
            item_num += 1
    print("\33[0;0;0m********************************************************")


# *** Main Routine ***
# Lists to hold data
item_names = []
item_prices = []
item_weights = []
item_worth = []
sorted_list = []
viable_ans = [["yes", "yup", "sure", "y"], ["no", "nope", "negative", "n"]]

# Starts program
print("Hello and welcome to the Price Comparison Program")
show_list = blank_check("Do you need instructions? >> ").lower()
valid = get_choice(show_list, viable_ans)
if not valid:
    print("Please enter with Y/N")
    print(show_list)  # Asks again
elif valid == "Yes":
    #  Instructions
    print("\33[1;0;1m\nThis program is intended to help you make a well"
          " educated decision if you are planning on buying something. "
          "\n\33[1;31;1mE.g. Chocolate, Coffee or Fizzy. \33[1;0;1m\n\n"
          "This Program will need 3 kinds of information for each item. "
          "\33[1;31;1mName, Price and Net Weight. \33[1;0;1m\n\nAfter "
          "entering all of the information for every item, press "
          "\33[1;31;1m'X' and 'enter' \33[1;0;1mto continue. "
          "\nThe program will then tell you which item is the best price"
          " for it's weight. \n\nYou can also choose to have a "
          "list of each item at the end if you do not agree with the "
          "choice.\33[0;0;0m")
    # Goes to next part of the program
    budget = int_check("\nWhat is your budget? >> $")
    print(f"Your budget is ${budget:,.2f}")
else:
    # Goes to next part of the program
    budget = int_check("What is your budget? >> $")
    print(f"Your budget is ${budget:,.2f}")

# Beginning the item information loop
item_info()
