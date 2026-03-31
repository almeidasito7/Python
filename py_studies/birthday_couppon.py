# A clothing store has a birthday promotion and granted a 10% discount for those who use the coupon NIVER10.

# Requesting customer data
print("")
print("WELCOME TO FIAP WEAR!")
print("----------------------")
print("")
purchase_value = float(input("Enter the purchase amount: "))
print("")
coupon = input("Enter the discount coupon: ")
print("")

# Performing logical test with the coupon in uppercase
    # Another option to solve this problem -> #if coupon == 'BIRTHDAY10' or coupon == 'birthday10':
if coupon.upper() == 'BIRTHDAY10':
    # Calculation of 10% discount
    total_value = float(purchase_value) * 0.9
    print("Your coupon was applied successfully!")
    print("")
else:
    total_value = float(purchase_value)
    print("Invalid coupon!")
    print("")

# Displaying the final value of the purchase
print("The total purchase value was $ {}".format(total_value))
print("")
