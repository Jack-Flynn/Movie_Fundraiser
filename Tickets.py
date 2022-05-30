
# Functions go here
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


def yesno (question):
    error = "Please enter yes or no"
    valid = False
    while not valid:
        try:
            response = input(question)
            if response in yes:
                break
            elif response in no:
                exit()
            else:
                print(error)
        except ValueError:
            print(error)


# Set up lists and variables
yes = ["yes", "y", "yep", "accept", "yeah", "yea"]
no = ["no", "n", "nope", "nah", "deny", "nay"]
ticket_prices = [7.50, 10.50, 6.50]
seat_count = 5

# Main routine goes here
while seat_count > 0:
    age = age_check("How old are you?", 12, 125)
    yesno("Do you want tickets?")

    if 12 <= age <= 15:
        ticket_price = ticket_prices[0]
    elif 16 <= age <= 64:
        ticket_price = ticket_prices[1]
    else:
        ticket_price = ticket_prices[2]

    # Print the results of everything
    print("if you are {} then that will cost ${:.2f}".format(age, ticket_price))
    seat_count -= 1
