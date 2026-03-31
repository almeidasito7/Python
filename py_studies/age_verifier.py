print("AGE VERIFIER")
print("--------------------")
print("")
name = str(input("Please enter the student's name: "))
# Ask for the student's age
age = int(input("Please enter the student's age: "))
# Check if the student is an adult
print("")
if age >= 18:
    print(f"Student {name} is of legal age!")
    print("")
else:
    print(f"Student {name} is not of legal age!")
    print("")
