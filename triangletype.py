def triangle_type(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilateral"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "Isoceles"
    else:
        return "Scalene"

side1 = input("Enter side 1:")
side2 = input("Enter side 2:")
side3 = input("Enter side 3:")

triangle = triangle_type(side1, side2, side3)

print("The triangle with {},{} and {} is {}".format(side1,side2,side3,triangle))