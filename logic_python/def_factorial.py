def factorial(a=0, show=False):
    e = 1
    for c in range(a, 0, -1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        e *= c
    return e


num = int(input("Enter a number: "))
print(f'{factorial(num, True)}')
