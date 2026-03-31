# Menu structure
option = -1 
grades = []
while option != 4:
    print("1-Register Grade\n2-Display Grades\n3-Calculate Average\n4-Exit")
    option = int(input("Enter the desired option: "))
    

    if option == 1:
        grade = float(input("Please enter the student's grade: "))
        print("-------------------------------------------")
        grades.append(grade)
    
    elif option == 2:
        print("REGISTERED GRADES:")
        print("------------------")
        for grade in grades:
            print(grade)


    elif option == 3:
        if len(grades) > 0:  # Check if there are registered grades
            total_sum = sum(grades)
            average = total_sum / len(grades)  # Calculate the average once
            print(f"Average of grades: {average}")
        else:
            print("No grades registered to calculate the average.")


    elif option == 4:
        print("Exiting...")
    else:
        print("Invalid Option!")
