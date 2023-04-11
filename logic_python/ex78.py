lista = []
max_pos = []
min_pos = []
for i in range(0, 5):
    lista.append(int(input(f"Digite um valor para posição {i}: ")))

for pos, val in enumerate(lista):
    if val == max(lista):
        max_pos.append(pos)
    if val == min(lista):
        min_pos.append(pos)


print(f'Você digitou os valores {lista}')
print(f"O maior valor digitado foi {max(lista)} nas posições {max_pos}")
print(f"O menor valor digitado foi {min(lista)} nas posições {min_pos}")
