i=0
lista=[]
n2 = []
n1 = []

while i < 1:
    x = int(input("Digite um número: "))
    y = input("Deseja continuar [y/n]: ")
    if y == "n":
        lista.append(x)
        i += 1
    elif y == "y":
        lista.append(x)
    else:
        break
for v in (lista):
    if v % 2 == 0:
        n2.append(v)
    elif v % 2 ==1:
        n1.append(v)
print(f"A lista completa é {lista}")
print(f'A lista de pares {n2}')
print(f'A lista de ímpares {n1}')

