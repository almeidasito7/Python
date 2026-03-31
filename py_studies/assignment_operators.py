print("ASSIGNMENT OPERATORS - ARITHMETIC")
print("--------------------------------------")

print("VALUE VIEWER")
print("----------------------")
value0 = int(input("Enter a value to view: "))
print(f"The value entered was {value0}")
print("------------------------")
print("")

print("VALUE ADDER")
print("------------------")
value1 = int(input("Enter the 1st value: "))
value2 = int(input("Enter the 2nd value: "))
sum_val = value1 + value2 
print(f"The sum of the values is: {sum_val}")
print("------------------------")
print("")

print("MULTI-OPERATORS")
print("----------------")
x = int(input("Enter the first value you want to calculate: "))
y = int(input("Enter the second value you want to calculate: "))

minus1 = x - y
sum1 = x + y
multi = x * y
division = x / y
rem_division = x % y
int_div = x // y 
expo = x ** y


print("")
print("Below are the results of the multi-operations: ")
print("")
print(f"Sum value: {sum1}")
print("")
print(f"Subtraction value: {minus1}")
print("")
print(f"Multiplication value: {multi}")
print("")
print(f"Division value: {division}")
print("")
print(f"Integer division value: {int_div}")
print("")
print(f"Remainder of division: {rem_division}")
print("")
print(f"Exponentiation value: {expo}")
print("------------------------------------------")
