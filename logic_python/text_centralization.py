def write(txt):
    size = len(txt) + 4
    print('~'*size)
    print(f'  {txt}')
    print('~'*size)


write("Hello world")
