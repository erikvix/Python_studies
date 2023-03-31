# Progressão aritmética

primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiro
cont = 1
while cont <= 10:
    print(termo, "->", end=' ')
    termo += razao
    cont += 1
print("ACABOU!")
