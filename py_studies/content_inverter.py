print("This program swaps the contents of two variables")
A = input("Enter the content of variable 1: ")
B = input("Enter the content of variable 2: ")
swap = A
A = B
B = swap
print("Now that we swapped, variable A contains {} and variable B contains {}".format(A, B))
