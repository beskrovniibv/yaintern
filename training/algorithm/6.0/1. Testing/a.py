x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
x, y = int(input()), int(input())


if x > x1 and x < x2:
    if y > y2:
        print("N")
    else:
        print("S")
elif y > y1 and y < y2:
    if x < x1:
        print("W")
    else:
        print("E")
elif x < x1:
    if y < y1:
        print("SW")
    else:
        print("NW")
else:
    if y < y1:
        print("SE")
    else:
        print("NE")
