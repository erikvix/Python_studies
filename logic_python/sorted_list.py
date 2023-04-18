num = a = 0
values = list()
for c in range(0, 5):
    num = int(input('Enter a value: '))
    if c == 0 or num > max(values):
        values.append(num)
        print('Added to the end of the list...')
    else:
        a = 0
        while num > a:
            if values[a] > num:
                break
            a += 1
        values.insert(a, num)
        print(f'Added at position {a} in the list')
print('-='*30)
print(f'The values entered in order were: {values}')
