def calculate_land_area():
    print("Land Area Calculator")
    print("-" * 21)


def calculate_area(width, length):
    print(f"The area of a land with {width}m x {length}m is {width*length}m²")


calculate_land_area()

width = float(input("WIDTH (m): "))
length = float(input("LENGTH (m): "))

calculate_area(width, length)
