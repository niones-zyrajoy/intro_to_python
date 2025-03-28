
num = int(input("Enter a two-digit number: "))
if 10 <= num <= 99:
    digit_sum = (num // 10) + (num % 10)
    print("The sum of the digits is:", digit_sum)
else:
    print("Please enter a valid two-digit number.")