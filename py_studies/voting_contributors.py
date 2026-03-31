# Exercise 1 - Evaluative Activity Chap. 3

# Variable that will serve to receive the option entered by the user
i = 0
option = -1
resp = str
print("Hello! We are conducting an internal vote with our employees to define a fixed day of the week for exclusive lives \nwith our Mentorship Team.\nPlease answer the survey below.")

qty = int(input("How many employees will participate in the voting?\nA:"))

# While the user does not enter option 4, the program will run
    # Display of menu options
while (i != qty):
    i = i + 1
    print("Employee #{}".format(i))
    print("")
    print("What would be the best day of the week for you to follow the lives with our Mentorship Team?")
    print("---------------------------------------------------------------------------------------------")
    print("1 - Monday")
    print("2 - Tuesday")
    print("3 - Wednesday")
    print("4 - Thursday")
    print("5 - Friday")

    option = int(input("Enter your availability: "))

    # Verification of available options 
    if option == 1:
    # What will happen if the option is 1
        print("Perfect! The chosen day of the week was Monday.")
    elif option == 2:
    # What will happen if the option is 2
        print("Perfect! The chosen day of the week was Tuesday.")
    elif option == 3:
    # What will happen if the option is 3
        print("Perfect! The chosen day of the week was Wednesday.")
    elif option == 4:
    # What will happen if the option is 4
        print("Perfect! The chosen day of the week was Thursday.")
    elif option == 5:
    # What will happen if the option is 5
        print("Perfect! The chosen day of the week was Friday.")
    # When the loop ends, display the message
