print("PLUS INTERNET SCORE PROGRAM")
print("-----------------------------------")

score = int(input("Enter the customer's score: "))
print("")
if (score >= 1000):
    print("Add another 3GB to the customer's internet plan.")
    print("")
else:
    if (score >= 500):
        print("Add another 1.5GB to the customer's internet plan.")
        print("")
    else:
        if (score >= 200):
            print("Add another 500MB to the customer's internet plan.")
            print("")
        else:
            print("The score entered has not reached the target to earn the bonus.")
            print("")        
