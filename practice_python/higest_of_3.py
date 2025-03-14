"""""
the user to enter three numbers and prints the highest number.
1. Prompts the user to enter the first number and converts it to an integer.
2. Prompts the user to enter the second number and converts it to an integer.
3. Prompts the user to enter the third number and converts it to an integer.
4. Uses the max() function to find the highest number among the three entered numbers.
5. Prints the highest number.
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
print("The highest number is:", max(num1, num2, num3))