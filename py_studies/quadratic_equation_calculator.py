import math

print("QUADRATIC EQUATION CALCULATOR")
print("----------------------------------")
print("")

# Requesting values for A, B, and C
a = float(input("Enter the value of A: "))
b = float(input("Enter the value of B: "))
c = float(input("Enter the value of C: "))

# Calculation of delta
delta = b * b / 4 * a * c

# Way to solve the problem with condition checks using nested if
#if delta > 0.0:
    # Calculation of 2 values for x
#    x1 = (-b + math.sqrt(delta)) / (2 * a)
#    x2 = (-b - math.sqrt(delta)) / (2 * a)
#    print("For the equation {}x² + {}x + {} = 0, we obtained the following values: x1 = {} and x2 = {}".format(a,b,c,x1,x2))
#    print("")
#else:
#    if delta == 0.0:
#        # Calculation of 1 value for x
#        x = (-b + math.sqrt(delta)) / (2 * a)
#        print("For the equation {}x² + {}x + {} = 0, we obtained the following value: x = {}".format(a,b,c,x))
#        print("")
#    else:
        # Display of a message
#        print("For the equation {}x² + {}x + {} = 0, there are no real values for x".format(a,b,c))
#        print("")


# Way to solve the problem with condition checks using elif 
if delta > 0.0:
# Calculation of 2 values for x
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("For the equation {}x² + {}x + {} = 0, we obtained the following values: x1 = {} and x2 = {}".format(a,b,c,x1,x2))
    print("")

elif delta == 0.0:
# Calculation of 1 value for x
    x = (-b + math.sqrt(delta)) / (2 * a)
    print("For the equation {}x² + {}x + {} = 0, we obtained the following value: x = {}".format(a,b,c,x))
    print("")

else:
# Display of a message
    print("For the equation {}x² + {}x + {} = 0, there are no real values for x".format(a,b,c))
    print("")    
