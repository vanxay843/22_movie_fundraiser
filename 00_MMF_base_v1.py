# import statements


# functions go here

# check the ticket name is not blank
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)

        # if name is not blank, program continues
        if response != "":
            return response

        # if name is blank, show error (& repeat loop)
        else:
            print("sorry - this can't be blank, "
                  "please enter your name")

# checks for an interger between two values
def int_check(question, low_num, high_num):
    error = "please enter a whole number between {} " \
            "and {}".format(low_num, high_num)

    valid = False
    while not valid:
        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if low_num <= response <= high_num:
                return response
            else:
                print(error)

        # if an integer is not entered, display an error
        except ValueError:
            print(error)

# ****** main routine ******

# set up dictionaries / lists needed to hold data

# ask user if they have used the program before & show instructions if necessary

# loop to get ticket details

# initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    # tells user how many tickets are left
    if count < 4:
        print("you have {} seats "
              "left".format(MAX_TICKETS - count))

    # warns user that only one seat is left!
    else:
        print("*** there is ONE seat left!! ***")

    # get details...

    # get name (can't be blank)
    name = not_blank("name: ")

    # end the loop if the exit code is entered
    if name == "xxx":
        break

    count += 1

   # get age (between 12 and 130)
    age = int_check("age: ")

   # check that age is valid...
   if age < 12:
       print("sorry you are too young for this movie")
       continue
   elif age > 130:
       print("that is very old - it looks like a mistake")
       continue


# end of tickets loop

#calculate profit etc...
if count == MAX_TICKETS :
    print("you have sold all the available tickets!")
else:
    print("you have sold {} tickets. \n"
          "there are {} places still available"
          .format(count, MAX_TICKETS - count))


    # get name (can't be blank)
    name = not_blank("name: ")


    # calculate ticket price

    # loop to ask for snacks

    # calculate snack price

    # ask for payment method (and apply surcharge if necessary)

# calculate total profit and sales

# output data to text file
