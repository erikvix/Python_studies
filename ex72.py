numeros = ("zero", "um", "dois", "três", "quatro", "cinco")
while True:
    x = int(input("Digite um número entre 0 e 5: "))
    if 0 <= x <= 5:
        break
    print("tente novamente")
print(f"voce digitou o numero {numeros[x]}")
