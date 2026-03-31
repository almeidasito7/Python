def main():
    # Ask how many employees will participate in the survey
    num_employees = int(input("How many employees will participate in the survey? "))

    # Dictionary to store vote counts for each day of the week
    voted_days = {
        "monday": 0,
        "tuesday": 0,
        "wednesday": 0,
        "thursday": 0,
        "friday": 0,
    }

    # Loop to collect votes from each employee
    for i in range(num_employees):
        print(f"\nEmployee {i + 1}:")
        chosen_day = input("Choose a day of the week (e.g., monday, tuesday, etc.): ").lower()
        
        # Check if the chosen day is valid and increment the vote count
        if chosen_day in voted_days:
            voted_days[chosen_day] += 1
        else:
            print("Invalid day of the week. Try again.")

    # Determine the most voted day
    most_voted_day = max(voted_days, key=voted_days.get)

    # Show the voting result
    print("\nVoting result:")
    print(f"The most voted day is: {most_voted_day}, with {voted_days[most_voted_day]} votes.")

if __name__ == "__main__":
    main()
