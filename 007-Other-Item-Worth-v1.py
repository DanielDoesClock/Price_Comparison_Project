"""This is the 6th component in my Price Comparison Project
This component will create a list with all item names and price
sorted by worth
Made By Daniel Fraser
28/05/22"""


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
    worth_list()


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


sorted_list = []
item_names = ["Venus Bar", "Softy Bar", "Freddo Flamingo"]
item_prices = ["2.30", "1.80", "5"]
item_worth = ["126", "122.22", "130"]
# Added all values to lists
budget = "4.60"
# so that I do not have to do it manually for every test
sort_items()
