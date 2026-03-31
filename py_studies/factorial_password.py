# Hacker attack and freedom password

minutes = int(input("Enter the current time minutes: "))

factorial = minutes

# Factorial calculation
for num in range(1, minutes):
    factorial = factorial * num

print(f"The password is FREEDOM{factorial}")
