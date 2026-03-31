print("SIMPLE CONDITION - SALARY AND EMPLOYEE")
print("--------------------------------------")
print("")
# Ask the user to enter the employee's name
name = input("Enter the employee's name: ")
# Ask the user to enter the employee's salary
salary = float(input("Enter the employee's salary: "))
if (salary < 0):
    # salary = salary * -1
    salary = abs(salary)
    print("Attention, a negative salary value was entered! Please review.")
print("")
print(f"Employee {name} has a salary of ${salary}")
print("")
