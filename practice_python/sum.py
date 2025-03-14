"""
This script prompts the user to enter a two-digit number and calculates the sum of its digits.
1. Prompts the user to enter a two-digit number and converts it to an integer.
2. Checks if the entered number is a valid two-digit number (between 10 and 99 inclusive).
3. If the number is valid, calculates the sum of its digits.
4. Prints the sum of the digits.
5. If the number is not valid, prints a message asking the user to enter a valid two-digit number.
"""
num = int(input("Enter a two-digit number: "))
if 10 <= num <= 99:
    digit_sum = (num // 10) + (num % 10)
    print("The sum of the digits is:", digit_sum)
else:
    print("Please enter a valid two-digit number.")