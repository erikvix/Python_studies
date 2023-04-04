i = 0
lista = []
n5 = []
while i < 1:
    x = int(input("Digite um número: "))
    y = input("Deseja continuar [y/n]: ")
    if y == "n":
        lista.append(x)
        i += 1
    if y == "y":
        lista.append(x)
    else:
        break
print(f'O tamanho da lista é de {len(lista)} números')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O número 5 não faz parte da lista')
