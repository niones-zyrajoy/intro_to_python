"""
vowel or consonant
1. Prompts the user to enter a character and converts it to lowercase.
2. Checks if the character is a vowel (a, e, i, o, u).
3. If the character is a vowel, prints "The character is a vowel."
4. If the character is not a vowel but is an alphabetic character, prints "The character is a consonant."
5. If the character is not an alphabetic character, prints "Invalid input."
"""

char = input("Enter a character: ").lower()
if char in 'aeiou':
    print("The character is a vowel.")
elif char.isalpha():
    print("The character is a consonant.")
else:
    print("Invalid input.")