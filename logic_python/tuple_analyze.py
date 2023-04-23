
test = ("2")
n1 = (int(input("Enter a number: ")),
      int(input("Enter a number: ")),
      int(input("Enter a number: ")),
      int(input("Enter a number: ")))
print(n1)
if 9 in n1:
    print(f"The value 9 appeared {n1.count(9)} times")
else:
    print(f"The value 9 did not appear")
if 3 in n1:
    print(f"The value 3 appeared at the {n1.index(3)+1}th position")
else:
    print(f"The value 3 did not appear")
print(f"The even values entered were ", end='')
for n in n1:
    if n % 2 == 0:
        print(n, end='')
