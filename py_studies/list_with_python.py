# Using lists in Python

# Creating our list
protein = ["Red meat", "Chicken", "Fish"] # Creating lists, items are indexed as: 0, 1, 2, 3....
print(protein)

# Displaying a specific value from our list
print(protein[2])
# Using for to display all items in the list
for name in protein:
    print(name)

print("-----------------------------------------------")
# Inserting items into the list through code
protein.append("Eggs")

for name in protein:
    print(name)

print("-----------------------------------------------")
# Inserting items into the list through user input
protein.append(input("Please add an item to the protein list: "))

for name in protein:
    print(name)

print("-----------------------------------------------")
# Inserting items into the list through code using index to indicate the position of the item
protein.insert(2, "Lamb meat")

for name in protein:
    print(name)

print("-----------------------------------------------")
# Inserting items into the list through user input using index to indicate the position of the item
protein.insert(2, input("Please add an item to the protein list: "))

for name in protein:
    print(name)
