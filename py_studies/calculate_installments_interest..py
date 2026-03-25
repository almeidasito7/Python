def installment_calculation(debt_amount, interest_rate, installments):
    interest_amount = debt_amount * interest_rate / 100
    total_value = debt_amount + interest_amount
    installment_value = total_value / installments
    return interest_amount, installment_value

def main():
    debt_amount = float(input("Enter the debt amount: "))

    print("\nInstallment Table:")

    # Define the quantity of installments and the interest rates
    installments_quantity = [1, 3, 6, 9, 12]
    interest_rates = [0, 10, 15, 20, 25]

    for installments, interest_rate in zip(installments_quantity, interest_rates):
        interest_amount, installment_value = installment_calculation(debt_amount, interest_rate, installments)
        print(f"Total:R$ {debt_amount:.2f}  Fees:R$ {interest_amount:.2f}   Number of installments:{installments}x   Installments Value:R$ {installment_value:.2f}")
if __name__ == "__main__":
    main()


