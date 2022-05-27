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
                    exit()
                else:
                    print("I'll assume that means no")
                    exit()
        except ValueError:
            print(error)


def ticket_calculation(question):
    error = "please enter yes or no"
    valid = False
    response = input(question).lower()
    while not valid:
        try:
            if question in yes:
                if 12 <= age <= 15:
                    tickets = ticket_prices[0]
                elif 16 <= age <= 64:
                    tickets = ticket_prices[1]
                else:
                    tickets = ticket_prices[2]
                return response
            elif question in no:
                exit()
        except ValueError:
            print(error)


yes = ["yes", "y", "yep", "accept", "yeah", "yea"]
no = ["no", "n", "nope", "nah", "deny", "nay"]
ticket_prices = [7.50, 10.5, 6.5]
seat_count = 150
while seat_count > 0:
    age = age_check("How old are you?", 12, 125)
    ticket_calculation("do you want tickets?")

    print("if you are {} then that will cost ${:.2f}".format(age, tickets))
    seat_count -= 1
