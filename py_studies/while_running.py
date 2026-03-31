# Variable that will serve to receive the option entered by the user
option = -1
# While the user does not enter option 4, the program will run
while (option != 4):
    # Display of menu options
    print("SUPER WONDERFUL PROGRAM")
    print("1 - Run code 1")
    print("2 - Run code 2")
    print("3 - Run code 3")
    print("4 - Exit the program")

    option = int(input("Enter your option: "))

    # Verification of available options 
    if option == 1:
        # What will happen if the option is 1
        print("CODE 1 RUNNING...")
    elif option == 2:
        # What will happen if the option is 2
        print("CODE 2 RUNNING...")
    elif option == 3:
        # What will happen if the option is 3
        print("CODE 3 RUNNING...")
# When the loop ends, display the message
print("OK! The program is closed...")
