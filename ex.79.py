lista = []
i = 0
while i < 1:
    x = int(input("Digite um valor: "))
    if x not in lista:
        lista.append(x)
    else:
        print("Número ja inserido")
    x = input("Quer continuar? [y/n]: ")

    if x == "n":
        i += 1
    elif x == "y":
        continue
    else:
        print("opção incorreta")
        i += 1
print(lista)
