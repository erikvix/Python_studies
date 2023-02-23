width = float(input("enter wall width: : "))
height = float(input("enter wall height: "))

area = (width * height)
paint = (area / 2)

print("Your wall has: {} m²".format(area))
print("to paint this wall you'll need {}L of paint".format(paint))