def calculate_installment(final_price, installments):
    percentage_increase = {
        6: 0.03,  # 3% increase for 6 installments
        12: 0.06,  # 6% increase for 12 installments
        18: 0.09,  # 9% increase for 18 installments
        24: 0.12,  # 12% increase for 24 installments
        30: 0.15,  # 15% increase for 30 installments
        36: 0.18,  # 18% increase for 36 installments
        42: 0.21,  # 21% increase for 42 installments
        48: 0.24,  # 24% increase for 48 installments
        54: 0.27,  # 27% increase for 54 installments
        60: 0.30   # 30% increase for 60 installments
    }
    addition = final_price * percentage_increase[installments]
    total_price = final_price + addition
    installment_price = total_price / installments
    return total_price, installment_price

def main():
    car_price = float(input("Enter the car value: "))

    final_value_seen = car_price * 0.8  # 20% discount for cash payment
    print(f"Final price for cash payment (20% discount): R$ {final_value_seen:.2f}")

    print("\nInstallment Table:")
    print("")
    for installments in range(6, 61, 6):
        total_price, installment_price = calculate_installment(car_price, installments)
        print(f"Total price for {installments} installments: R$ {total_price:.2f}")
        print(f"Installment price for {installments} installments: R$ {installment_price:.2f}")
        print("")

if __name__ == "__main__":
    main()