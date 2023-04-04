lista = [[], []]

for c in range(0, 7):
    valor = int(input(f"Digite o {c+1} número: "))
    if valor % 2 == 0:
        lista[0].append(valor)
    elif valor % 2 == 1:
        lista[1].append(valor)

print(f"os valores pares digitados foram {lista[0]}")
print(f"os valores ímpares digitados foram {lista[1]}")
