# ex67

x = int(input("Enter a number: "))
while True:
    if x < 0:
        print("Incorrect number")
        break

    for i in range(1, 11):
        print(f"{x} x {i} = {x*i}")
    x = int(input("Enter other number: "))
