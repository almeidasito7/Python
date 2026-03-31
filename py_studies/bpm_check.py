print("BPM CHECK")
print("------------")
print("")

print("Attention, provide the data correctly to obtain an accurate result.")
print("-----------------------------------------------------------------------")
print("")

age = int(input("Enter your age: "))
print("")
bpm = int(input("Enter your BPM (Beats per Minute): "))
print("-------------------------------------------")


# Logical test for small children and babies with 120 bpm to 140 bpm
if age <= 2 and bpm >= 120 and bpm <= 140:
    print("Your heart rate is within the appropriate range.")
    print("")
elif bpm < 120:
    print("Your heart rate is below the appropriate range.")
    print("")
elif bpm > 140:
    print("Your heart rate is above the appropriate range.")
    print("")
    
# Logical test for children and youth with 80 bpm to 100 bpm
elif age >= 8 and age <= 18 and bpm >= 80 and bpm <= 100:
    print("Your heart rate is within the appropriate range.")
    print("")
elif bpm < 80:
    print("Your heart rate is below the appropriate range.")
    print("")
elif bpm > 100:
    print("Your heart rate is above the appropriate range.")
    print("")

# Logical test for sedentary adults with 70 bpm to 80 bpm
elif age < 65 and bpm >= 70 and bpm <= 80:
    print("Your heart rate is within the appropriate range.")
    print("")
elif bpm < 70:
    print("Your heart rate is below the appropriate range.")
    print("")
elif bpm > 80:
    print("Your heart rate is above the appropriate range.")
    print("")

# Logical test for seniors with 50 bpm to 60 bpm
elif age >= 65 and bpm >= 50 and bpm <= 60:
    print("Your heart rate is within the appropriate range.")
    print("")
elif bpm < 80:
    print("Your heart rate is below the appropriate range.")
    print("")
elif bpm > 100:
    print("Your heart rate is above the appropriate range.")
    print("")
