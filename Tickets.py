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


yes = ["yes", "y", "yep", "accept", "yeah", "yea"]
no = ["no", "n", "nope", "nah", "deny", "nay"]
ticket_prices = ["7.50", "10.50", "6.50"]


age = age_check("How old are you?", 12, 125)

if age >= 12 <= 15:
    tickets = ticket_prices[0]
elif age >= 16 <= 64:
    tickets = ticket_prices[1]
else:
    tickets = ticket_prices[2]

print("if you are {} then that will cost {}".format(age, tickets))
