def age_check(question, low_num, high_num):

    error = "Please enter a whole number between {} and {}".format(low_num, high_num)

    valid = False
    while not valid:

        try:
            response = int(input(question))

            if low_num <= response <= high_num:
                return response
            else:
                try_again = input("This value is outside the range (12, 125), did you want to re input your response?").lower()
                if try_again in yes:
                    print(error)
                elif try_again in no:
                    break
                else:
                    print("I'll assume that means no")
                    break
        except ValueError:
            print(error)


def blank_check(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response
        else:
            print("Your answer cannot be blank, please try again.")


yes = ["yes", "y", "yep", "accept", "yeah", "yea"]
no = ["no", "n", "nope", "nah", "deny", "nay"]

name = blank_check("What is your name?").title()

age = age_check("How old are you?", 12, 125)

