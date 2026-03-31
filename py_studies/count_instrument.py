instrument_list = ["Drums", "Guitar", "Acoustic Guitar", "Guitar", "Bass"]

print(instrument_list)

# What is the size of my list?
print(len(instrument_list))

# How many times does the element "Guitar" appear?
print(instrument_list.count("Guitar"))


# How to change the order of elements in the list?
instrument_list.reverse()
print(instrument_list)

# Sort list in ascending order (A-Z)
instrument_list.sort()
print(instrument_list)

# Sort list in descending order (Z-A)
instrument_list.sort(reverse=True)
print(instrument_list)
