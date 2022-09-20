# function goes here


# checks for an integer more than 0
def int_check(question):

    error = "please enter an whole number that is more than 11 and less than 131"

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)

test = int_check("please enter a number")
