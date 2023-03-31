x = soma = cont = 0
x = int(input("Digite um número [999 para parar]: "))
while x != 999:
    cont += 1
    soma += x
    x = int(input("Digite um número [999 para parar]: "))
print(f"Você digitou {cont} números e a soma entre eles é {soma}")
