# Childhood Education Project - App for financial control

# Enter how many transactions you performed
transaction_qty = int(input("Enter how many transactions you performed today: "))
total_transactions = 0
# What is the type of the transaction

# What are the values of the transactions
for transaction_n in range(1, transaction_qty + 1, 1):
    transaction = float(input("Please enter the value of transaction #{}: ".format(transaction_n)))
    total_transactions = total_transactions + transaction

average = total_transactions / transaction_qty

# Final summary
print("On this day, a total of ${} was spent, with an average of ${} per transaction".format(total_transactions, average))
