from function_calculator import *

option = -1
while (option != 5):
    print("1 - Sum two values")
    print("2 - Subtract two values")
    print("3 - Divide two values")
    print("4 - Multiply two values")
    print("5 - Exit")
    option = int(input("Enter your option: "))

    if option == 1:
        print(sum_vals(float(input("Enter the first value: ")), float(input("Enter the second value: "))))
    elif option == 2:
        print(subtract(float(input("Enter the first value: ")), float(input("Enter the second value: "))))
    elif option == 3:
        print(divide(float(input("Enter the first value: ")), float(input("Enter the second value: "))))
    elif option == 4:
        print(multiply(float(input("Enter the first value: ")), float(input("Enter the second value: "))))
    elif option == 5:
        print("Exiting")
    else:
        print("Invalid Option")
