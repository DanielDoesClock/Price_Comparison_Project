"""This is the 5th component in my Price Comparison Project
This second version will give the user more options then 'Y' and 'N'
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
                            "listed by worth? >> ").lower()
    yes_ans = ["yes", "yup", "sure", "y"]
    no_ans = ["no", "nope", "negative", "n"]
    if show_list in yes_ans:
        print("Continues to next part of code")  # Temp message
    elif show_list in no_ans:
        print("End of program")  # Temp message
    else:
        print("Invalid answer")
        ask_user()


# Main Routine
ask_user()
