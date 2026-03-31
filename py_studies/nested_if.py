print("NESTED IF IN PYTHON")
print("----------------------")
print("")

RM = int(input("Please enter your RM: "))
print("")
age = int(input("Please enter your age: "))
print("")

if (age >= 18):
    print(f"Your participation has been authorized, student with RM {RM}")
    print("More information will be sent to the registered email.")
    print("")
else:
    authorization = (input("Do you have authorization from your guardians? [Y-YES / N-NO]"))
    if (authorization == 'Y'):
        print("Your participation has been authorized, Student with RM {}!".format(RM))
        print("More information will be sent to the registered email.")
        print("")
    else:
        print("Unfortunately, your participation was not authorized due to your age.")
        print("")
