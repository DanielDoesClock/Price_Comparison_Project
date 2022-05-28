"""This is the 5th component in my Price Comparison Project
This third version will be using a nested list
Made By Daniel Fraser
28/05/22"""


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


# Main Routine
ask_user()
