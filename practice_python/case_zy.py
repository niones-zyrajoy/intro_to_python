print("\n                EXERCISES                  ")
print("---------------------------------------------")
print("1. Are the numbers equal or not              ")
print("2. Is the number odd, even or zero           ")
print("3. The highest number among the three numbers")
print("4. Quadrant of a coordinate                  ")
print("5. Vowel or Consonant                        ")
print("6. Sum of the digits of a two-digit number   ")
print("7. Exit                                      ")
print("---------------------------------------------")
choice = int(input("Enter choice: "))

match int(choice):
    case 1:
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter second number: "))
        if num_1 == num_2:
            print("The numbers are equal.")
        else:
            print("The numbers are not equal.")

    case 2:
        num = int(input("Enter a number: "))
        if num == 0:
            print("The number is zero.")
        elif num % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")

    case 3:
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter second number: "))
        num_3 = int(input("Enter third number: "))

        if num_1 >= num_2 and num_1 >= num_3:
            highest = num_1
        elif num_2 >= num_1 and num_2 >= num_3:
            highest = num_2
        else:
            highest = num_3
        print("The highest number is:", highest)

    case 4:
        x_axis = int(input("Enter x coordinate: "))
        y_axis= int(input("Enter y coordinate: "))

        if x_axis == 0 and y_axis == 0:
            print("The coordinate is at the Origin.")
        elif x_axis == 0:
            print("The coordinate is on the Y-axis.")
        elif y_axis == 0:
            print("The coordinate is on the X-axis.")
        elif x_axis > 0 and y_axis > 0:
            print("The coordinate is in Quadrant I.")
        elif x_axis < 0 and y_axis > 0:
            print("The coordinate is in Quadrant II.")
        elif x_axis < 0 and y_axis < 0:
            print("The coordinate is in Quadrant III.")
        elif x_axis > 0 and y_axis < 0:
            print("The coordinate is in Quadrant IV.")

    case 5:
        char = input("Enter a character: ").lower()  # Convert input to lowercase

        if char in 'aeiou':
            print("The character is a vowel.")
        elif char in 'bcdfghjklmnpqrstvwxyz':
            print("The character is a consonant.")
        else:
            print("Invalid input.")

    case 6:
        two_digit = int(input("Enter a two-digit number: "))
        if 10 <= num <= 99:
            digit_sum = (two_digit // 10) + (two_digit % 10)
            print("The sum of the digits is:", digit_sum)
        else:
            print("Please enter a valid two-digit number.")
            
    case 7:
        print("Exit")


