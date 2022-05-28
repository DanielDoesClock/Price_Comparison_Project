"""This is the 5th component in my Price Comparison Project
This component will ask the user if they want to see a list of the other items
Made By Daniel Fraser
28/05/22"""


def blank_check(ask_value):
    while True:
        response = input(ask_value).title()
        if not response:    # Checks if name has at least 1 letter
            print("***Please do not leave this blank!***")    # Error message
        else:
            return response    # Returns name


def ask_user():
    show_list = blank_check("Would you like a list of all other items "
                            "listed by worth? >> ").upper()
    if show_list == 'Y':
        print("Continues to next part of code")  # Temp message
    elif show_list == 'N':
        print("End of program")  # Temp message
    else:
        print("Please use 'Y' or 'N'")
        ask_user()


# Main Routine
ask_user()
