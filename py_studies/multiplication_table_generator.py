# MULTIPLICATION TABLE GENERATOR
i = 1
number = int(input("Please enter the value for which you want the multiplication table: "))

while (i <= 10):
    result = number * i
    print(f"{number} x {i} = {result}")
    i = i + 1
print("-----------------------------------------------------")

# Multiplication table with for - type 1
n = int(input("Enter the desired value to get the multiplication table: "))
for count in range(1, 10, 1):
    print(count * n)

print("-----------------------------------------------------")
# Multiplication table with for - type 2
nt = int(input("Enter the desired value to get the multiplication table: "))
for count_t in range(nt, nt * 10 + 1, nt):
    print(count_t)
