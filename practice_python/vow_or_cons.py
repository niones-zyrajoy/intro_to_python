
char = input("Enter a character: ").lower()  # Convert input to lowercase

if char in 'aeiou':
    print("The character is a vowel.")
elif char in 'bcdfghjklmnpqrstvwxyz':
    print("The character is a consonant.")
else:
    print("Invalid input.")