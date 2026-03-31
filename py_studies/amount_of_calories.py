# How many foods and how many calories did the user consume?

food_qty = int(input("Enter how many foods you consumed today: "))

total_calories = 0

# Adding the loop using for and range
for food in range(1, food_qty + 1, 1):
    calories = int(input("Enter the calorie amount for food item #{}: ".format(food)))
    total_calories = total_calories + calories

# Algorithm result
print("A total of {} calories were consumed throughout the day".format(total_calories))
