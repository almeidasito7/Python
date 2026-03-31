# First function in Python


# Function that calculates average speed
def calculate_average_speed(distance, time):
    
    # Calculate average speed
    average_speed = distance / time

    # Return the result
    return average_speed

# Main program starts here
dist = float(input("Enter the distance: "))
time = float(input("Enter the time: "))

# Calling the function with user-defined values
print("The average speed is {}".format(calculate_average_speed(dist, time)))
