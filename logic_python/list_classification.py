values = []
odd_numbers = []
even_numbers = []
while True:
    x = int(input("Enter a number: "))
    values.append(x)
    y = input("Do you want to continue? [y/n]: ")
    if y.lower() == "n":
        break

for v in values:
    if v % 2 == 0:
        odd_numbers.append(v)
    else:
        even_numbers.append(v)

print(f"The list of even numbers: {odd_numbers}")
print(f"The list of odd numbers: {even_numbers}")
print(f"The list has {len(values)} numbers")
values.sort(reverse=True)
print(values)
if 5 in values:
    print("The value 5 is in the list")
else:
    print("The value 5 is not in the list")
