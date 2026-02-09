# module4.py

# Ask the user how many numbers they want to type in
# N should be a positive integer
while True:
    try:
        N = int(input("Hey! How many numbers do you want to enter? (N, must be positive): "))
        if N > 0:
            break
        else:
            print("Hmm, that’s not positive. Please enter a positive number!")
    except ValueError:
        print("Oops! That’s not a number. Please type a positive integer.")

# Make a list to store the numbers
numbers = []

print(f"Cool! Now enter {N} numbers, one by one (only positive numbers allowed):")

# Loop through and get each number from the user
for i in range(N):
    while True:  # keep asking until a valid positive number is entered
        try:
            num = int(input(f"Enter number {i + 1}: "))
            if num >= 0:
                numbers.append(num)
                break  # exit loop once valid
            else:
                print("Oops! Only positive numbers are allowed. Try again.")
        except ValueError:
            print("Oops! That’s not a number. Please type an integer.")

# Ask the user which number they want to search for
while True:
    try:
        X = int(input("Which number do you want to find? (X can be any integer): "))
        break
    except ValueError:
        print("Oops! That’s not a number. Please type an integer.")

# We'll use this variable to store the index if we find X
found_index = -1  # -1 means 'not found'

# Go through all numbers and check if any matches X
for i in range(len(numbers)):
    if numbers[i] == X:
        found_index = i + 1  # +1 because we want positions starting from 1
        break  # stop looking once we find it

# Print the result in a friendly way
if found_index == -1:
    print(f"Oops! The number {X} is not in your list. Output: -1")
else:
    print(f"Yay! The number {X} is at position {found_index} in your list.")
