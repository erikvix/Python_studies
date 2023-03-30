x = int(input("Enter a number: "))
y = 0
for i in range(1, x + 1):
    if x % i == 0:
        print('\033[32m', end='')
        y += 1

    else:
        print('\033[31m', end='')
    print(i, end=' ')

print(f"\n\033[m{x} was divided {y} times")
if y == 2:
    print("\n\033[mThe number is prime")
else:
    print("The number is not prime")
