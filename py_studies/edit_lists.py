# Using lists in Python

# Creating our list
protein = ["Red meat", "Chicken", "Fish", "Eggs", "Whey Protein"] # Creating lists, items are indexed as: 0, 1, 2, 3....
print(protein)

# Removing the last item from the list
protein.pop()

# Using for to display all items in the list
for item in protein:
    print(item)

# Removing a specific value from the list
protein.pop(2)
for item in protein:
    print(item)

# Removing a specific value from the list
protein.remove("Fish")
for item in protein:
    print(item)
