i1 = int(input("Enter the first int: "))
i2 = int(input("Enter the second int: "))
i3 = int(input("Enter the third int: "))
if (i1 + i2) < i3:
    print("Can not draw a triangle.")
elif (i1 + i3) < i2:
    print("Can not draw a triangle.")
elif (i2 + i3) < i1:
    print("Can not draw a triangle.")
else:
    print("Triangle can be drawn.")