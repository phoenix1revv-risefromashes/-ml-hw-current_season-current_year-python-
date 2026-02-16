# module5_call.py
#This file contains the actual running code that uses the classes from module5_mod.py

from module5_mod import NumberList  # import the class

# Ask user for N
while True:
    try:
        N = int(input("How many numbers do you want to enter? (N, must be positive): "))
        if N > 0:
            break
        else:
            print("Please enter a positive integer!")
    except ValueError:
        print("Oops! That’s not a number.")

# Create object of NumberList class
my_list = NumberList()
my_list.read_numbers(N)

# Ask for the number to search
while True:
    try:
        X = int(input("Which number do you want to find? (X can be any integer): "))
        break
    except ValueError:
        print("Oops! That’s not a number.")

# Search and print result
result = my_list.find_number(X)
if result == -1:
    print(f"The number {X} was not found. Output: -1")
else:
    print(f"The number {X} was found at position {result}.")
