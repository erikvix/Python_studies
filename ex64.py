x = soma = cont = media = maior = menor = 0
alt = "s"

while alt == "s":
    x = int(input("Digite um número: "))
    soma += x
    cont += 1
    media = soma / cont
    if cont == 1:
        maior = menor = x
    else:
        if x > maior:
            maior = x
        elif x < menor:
            menor = x

    alt = str(input("Quer continuar? [s/n]: "))
print(f"Você digitou {cont} números e a média foi {media}")
print(f"O maior número foi {maior} e o menor número foi {menor}")
