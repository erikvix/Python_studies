i = 0
values = []
odd = []
even = []
while i < 1:
    x = int(input("Enter a number: "))
    y = input("Do you wish to continue [y/n]: ")
    if y == "n":
        values.append(x)
        i += 1
    if y == "y":
        values.append(x)
    else:
        break
    for v in (values):
        if v % 2 == 0:
            odd.append(v)
        elif v % 2 == 1:
            even.append(v)

print(f'The list of even numbers: {odd}')
print(f'The list of odd numbers: {even}')
print(f'The size of the list is {len(values)} numbers')
values.sort(reverse=True)
print(values)
if 5 in values:
    print('The value 5 is part of the list')
else:
    print('The number 5 is not part of the list')
