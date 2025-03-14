"""
checks if it is zero, even, or odd.
1. Prompts the user to enter a number.
2. Converts the input to an integer.
3. Checks if the number is zero.
4. If the number is zero, prints "The number is zero."
5. If the number is not zero, checks if it is even by using the modulus operator.
6. If the number is even, prints "The number is even."
7. If the number is not even, prints "The number is odd.""
"""
num = int(input("Enter a number: "))
if num == 0:
    print("The number is zero.")
elif num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")