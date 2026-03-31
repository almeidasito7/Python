# Algorithm input--------------------------------------------------------------------------------------
print("WELCOME TO ALMEIDA AIRLINES")
print("----------------------------")
print("")

print("ATTENTION! Fill in all information carefully and correctly.")
print("")


# Declared variables--------------------------------------------------------------------------------------

local_v = str
idata_v = int
rdata_v = int
pag_v = str

# Customer data request---------------------------------------------------------------------------
# Personal data
name = str(input("Enter your full name: "))
email = str(input("Enter your email: "))

# Trip data
trip_value = float(input("Enter the total ticket price: "))
print("")
people_qty = int(input("Enter the number of people on this trip: "))
print("")
class_v = int(input("What class will be chosen?\n1-Economy Class\n2-Business Class\n3-First Class\nEnter the desired class: "))
print("")
seat = int(input("Which area would you like to select your seat in?\n1-Front of Plane\n2-Middle of Plane\n3-Back of Plane: "))


# Logical test------------------------------------------------------------------------------------------------
# print(f"The total trip value is: ${trip_value}")




# Economy class discount
if class_v == 1 and people_qty == 2:
    trip_discount = trip_value * 3/100
    final_value = trip_value - trip_discount
    print("For this package, we offer the following commercial condition, with the discount already applied: ")
    print(f"TOTAL TRIP VALUE: ${final_value}")
    print("")
elif class_v == 1 and people_qty == 3:
    trip_discount = trip_value * 4/100
    final_value = trip_value - trip_discount
    print("For this package, we offer the following commercial condition, with the discount already applied: ")
    print(f"TOTAL TRIP VALUE: ${final_value}")
    print("")
elif class_v == 1 and people_qty >= 4:
    trip_discount = trip_value * 5/100
    final_value = trip_value - trip_discount
    print("For this package, we offer the following commercial condition, with the discount already applied: ")
    print(f"TOTAL TRIP VALUE: ${final_value}") 
    print("")

# Business class discount
elif class_v == 2 and people_qty == 2:
    trip_discount = trip_value * 5/100
    final_value = trip_value - trip_discount
    print("For this package, we offer the following commercial condition, with the discount already applied: ")
    print(f"TOTAL TRIP VALUE: ${final_value}")
    print("")
elif class_v == 2 and people_qty == 3:
    trip_discount = trip_value * 7/100
    final_value = trip_value - trip_discount
    print("For this package, we offer the following commercial condition, with the discount already applied: ")
    print(f"TOTAL TRIP VALUE: ${final_value}")
    print("")
elif class_v == 2 and people_qty >= 4:
    trip_discount = trip_value * 8/100
    final_value = trip_value - trip_discount
    print("For this package, we offer the following commercial condition, with the discount already applied: ")
    print(f"TOTAL TRIP VALUE: ${final_value}")
    print("") 

# First class discount
elif class_v == 3 and people_qty == 2:
    trip_discount = trip_value * 10/100
    final_value = trip_value - trip_discount
    print("For this package, we offer the following commercial condition, with the discount already applied: ")
    print(f"TOTAL TRIP VALUE: ${final_value}")
    print("")
elif class_v == 3 and people_qty == 3:
    trip_discount = trip_value * 15/100
    final_value = trip_value - trip_discount
    print("For this package, we offer the following commercial condition, with the discount already applied: ")
    print(f"TOTAL TRIP VALUE: ${final_value}")
    print("")
elif class_v == 3 and people_qty >= 4:
    trip_discount = trip_value * 20/100
    final_value = trip_value - trip_discount
    print("For this package, we offer the following commercial condition, with the discount already applied: ")
    print(f"TOTAL TRIP VALUE: ${final_value}")
    print("") 

else:
    print("System error, check the entered information.")
    print("")
