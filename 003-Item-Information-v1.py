"""This is the 2nd component of my price comparison project.
This first version will ask the user for the name, price and net weight of
the product.
Made by Daniel Fraser
13/05/22"""

item_names = []
item_prices = []
item_weights = []
more_items = "Y"

while more_items == "Y":
    name = input("What is the name of the product? >> ")
    item_names.append(name)
    price = input(f"What is the price of one {name}? >> ")
    item_prices.append(price)
    weight = input(f"What is the weight of one {name}? >> ")
    item_weights.append(weight)
    more_items = input("Do you want to compare more items? >> ").upper()

print(item_names)
print(item_prices)
print(item_weights)
