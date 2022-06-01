"""This is my 7th component for my Project Comparison project
This component will ask the user if they would like to receive some
instructions. If yes, it shows, in no it doesn't
Made by Daniel Fraser
30/05/22"""


def blank_check(ask_value):
    while True:
        response = input(ask_value).title()
        if not response:    # Checks if name has at least 1 letter
            print("***Please do not leave this blank!***")    # Error message
        else:
            return response    # Returns name


# Function to validate a response
def get_choice(choice, valid_choices):
    choice_error = "Sorry, that is not a valid choice"
    for list_item in valid_choices:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    print(choice_error)


def instructions():
    show_list = blank_check("Do you need instructions? >> ").lower()
    # Nested list for yes and no oriented answers
    viable_ans = [["yes", "yup", "sure", "y"], ["no", "nope", "negative", "n"]]
    valid = get_choice(show_list, viable_ans)
    if not valid:
        print("Please enter with Y/N")
        instructions()  # Asks again
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
        budget = int(input("\nWhat is your budget? >> $"))
        print(f"Your budget is ${budget:,.2f}")
    else:
        # Goes to next part of the program
        budget = input("What is your budget? >> $")
        print(f"Your budget is ${budget:,.2f}")


print("Hello and welcome to the Price Comparison Program")
instructions()
