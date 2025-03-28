
x_coordinate = int(input("Enter x coordinate: "))
y_coordinate = int(input("Enter y coordinate: "))
if x_coordinate > 0 and y_coordinate > 0:
    print("The coordinate is in Quadrant I.")
elif x_coordinate < 0 and y_coordinate > 0:
    print("The coordinate is in Quadrant II.")
elif x_coordinate < 0 and y_coordinate < 0:
    print("The coordinate is in Quadrant III.")
elif x_coordinate > 0 and y_coordinate < 0:
    print("The coordinate is in Quadrant IV.")
else:
    print("The coordinate is on the axis.")