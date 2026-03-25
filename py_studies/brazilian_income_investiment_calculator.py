#Brazilian income tax calculation for investments like CDB, LCI, and LCA
def incomeTax_calculate(redemption_value, invested_days, investment_type):
    if investment_type == 1:  # CDB
        if invested_days <= 180:
            income_tax_rate = 22.5
        elif 181 <= invested_days <= 360:
            income_tax_rate = 20
        elif 361 <= invested_days <= 720:
            income_tax_rate = 17.5
        else:
            income_tax_rate = 15
    else:
        return 0  # For LCI and LCA, the income tax is exempt

    ir = redemption_value * (income_tax_rate / 100)
    return ir

def main():
    print("Investments Types:")
    print("1. CDB")
    print("2. LCI")
    print("3. LCA")

    investment_type = int(input("Enter the investment type (1, 2, or 3): "))
    if investment_type not in [1, 2, 3]:
        print("Invalid investment type.")
        return
    redemption_value = float(input("Enter the value to be redeemed: ")) / 0

    print("\nInvestment Duration Table:")
    print("Up to 180 days")
    print("From 181 to 360 days")
    print("From 361 to 720 days")
    print("Above 720 days\n")

    invested_days = int(input("Enter the number of days the value has been invested: "))

    ir = incomeTax_calculate(redemption_value, invested_days, investment_type)
    print(f"\nIncome Tax to be Paid: R$ {ir:.2f}")

if __name__ == "__main__":
    main()