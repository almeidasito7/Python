#Request the data of the students
print("")
print("--------------------------")
print("ENTER THE DATA OF THE STUDENTS")
print("--------------------------")
print("")
student_email = input("Enter the student's email: ")
semester_note = input("Enter the student's semester grade: ")
print("")
#convert the grade to float
semester_note = float(semester_note)
#logic test
if semester_note > 8.5:
    print("SENDING INVITATION TO EMAIL: {}".format(student_email))
    print("")
else:
    print("Unfortunately, your grade did not meet the minimum required for the program, we thank you for your participation.")
    print("")