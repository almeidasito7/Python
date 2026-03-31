# Fibonacci luck algorithm

# User enters the number
user_num = int(input("Please enter an integer: "))

# Base of the Fibonacci sequence
previous1 = 1
previous2 = 0

# Sequence calculation
for element_n in range(1, user_num + 1, 1):
    current_val = previous1 + previous2
    previous1 = previous2
    previous2 = current_val
    print(current_val)
    if user_num == current_val:
        print("Action Successful!")
        break
    elif user_num <= current_val:
        print("Action Failed!")
        break
