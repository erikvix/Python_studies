lst = []
for i in range(1, 6):
    x = float(input(f'Peso da {i}ª pessoa: '))
    lst += [x]
print('')
print('O Maior peso foi:', max(lst))
print('O Menor peso foi:', min(lst))
