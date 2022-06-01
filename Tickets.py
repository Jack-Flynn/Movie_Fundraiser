# Functions go here
def age_check(question):
    error = "Please enter a whole number between 12 and 125"
    valid = False
    while not valid:

        try:
            response = int(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


# Set up lists and variables
yes = ["yes", "y", "yep", "accept", "yeah", "yea"]
no = ["no", "n", "nope", "nah", "deny", "nay"]

seats_remaining = 5
ticket_count = 0
ticket_sales = 0

while ticket_count < seats_remaining:
    # Tells user how many tickets left
    if ticket_count < seats_remaining - 1:
        print("You have {} places left".format(seats_remaining - ticket_count))
    # One place left
    else:
        print("***You have ONE place left***")

    # Get age (between 12 and 130)
    age = age_check("Age: ")

    # Check age of person
    if age < 12:
        print("Sorry you are too young for this movie")
        continue
    elif age > 125:
        print("That is very old, it looks like a mistake")
        continue

    # Adjust ticket price based on age
    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    print("That will cost {}".format(ticket_price))
    ticket_count += 1
    ticket_sales += ticket_price

    print("We have currently sold {} worth of tickets".format(ticket_sales))

print("We are out of seats now!")
