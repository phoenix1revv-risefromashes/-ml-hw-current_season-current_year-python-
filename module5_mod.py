# module5_mod.py
#this file containesl only the class and no running code

class NumberList:
    def __init__(self):
        self.numbers = []

    def read_numbers(self, N):
        print(f"Enter {N} numbers one by one (only positive numbers allowed):")
        for i in range(N):
            while True:
                try:
                    num = int(input(f"Enter number {i + 1}: "))
                    if num >= 0:
                        self.numbers.append(num)
                        break
                    else:
                        print("Oops! Only positive numbers are allowed. Try again.")
                except ValueError:
                    print("Oops! That’s not a number. Please type an integer.")

    def find_number(self, X):
        for i, num in enumerate(self.numbers):
            if num == X:
                return i + 1  # 1-based index
        return -1
