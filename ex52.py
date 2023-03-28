x = int(input("Digite um número: "))
y = 0
for i in range(1, x + 1):
    if x % i == 0:
        print('\033[32m', end='')
        y += 1

    else:
        print('\033[31m', end='')
    print(i, end=' ')

print(f"\n\033[mo número {x} foi dividido {y} vezes")
if y == 2:
    print("\n\033[mO número é primo")
else:
    print("O número não é primo")
