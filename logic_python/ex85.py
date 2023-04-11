lista = []
dados = []
mai = men = 0
while True:
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Peso: ")))
    if len(lista) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    lista.append(dados[:])
    dados.clear()
    y = input("Deseja continuar [y/n]: ")
    if y in "Nn":
        break


print("-="*30)
print(f"Ao todo você cadastrou {len(lista)} pessoas")
print(f"O maior peso foi de {mai}.")
for p in lista:
    if p[1] == mai:
        print(f'{p[0]}')
    elif p[1] == men:
        print(f'{p[0]}')
print(f"O menor peso foi de {men}. peso de ")
