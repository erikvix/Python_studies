num = a = 0
valores = list()
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > max(valores):
        valores.append(num)
        print('Adicionado ao final da lista...')
    else:
        a = 0
        while num > a:
            if valores[a] > num:
                break
            a += 1
        valores.insert(a, num)
        print(f'Adicionado na posição {a} da lista')
print('-='*30)
print(f'Os valores digitados em ordem foram {valores}')