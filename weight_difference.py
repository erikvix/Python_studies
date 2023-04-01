lst = []
for i in range(1, 6):
    x = float(input(f"{i}ª person's weight: "))
    lst += [x]
print('')
print('the heavier weight was:', max(lst))
print('the lighter weight was:', min(lst))
