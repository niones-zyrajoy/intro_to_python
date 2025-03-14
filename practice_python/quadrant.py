""""
1. Prompts the user to enter the x coordinate and converts it to an integer.
2. Prompts the user to enter the y coordinate and converts it to an integer.
3. Checks if the point is in Quadrant I (x > 0 and y > 0).
4. If the point is in Quadrant I, prints "The coordinate is in Quadrant I."
5. Checks if the point is in Quadrant II (x < 0 and y > 0).
6. If the point is in Quadrant II, prints "The coordinate is in Quadrant II."
7. Checks if the point is in Quadrant III (x < 0 and y < 0).
8. If the point is in Quadrant III, prints "The coordinate is in Quadrant III."
9. Checks if the point is in Quadrant IV (x > 0 and y < 0).
10. If the point is in Quadrant IV, prints "The coordinate is in Quadrant IV."
11. If the point is not in any quadrant (i.e., it is on one of the axes), prints "The coordinate is on the axis."
"""""
x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))
if x > 0 and y > 0:
    print("The coordinate is in Quadrant I.")
elif x < 0 and y > 0:
    print("The coordinate is in Quadrant II.")
elif x < 0 and y < 0:
    print("The coordinate is in Quadrant III.")
elif x > 0 and y < 0:
    print("The coordinate is in Quadrant IV.")
else:
    print("The coordinate is on the axis.")