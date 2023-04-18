matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = terceira_coluna = segunda_linha = 0


for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(
            input(f"Digite o valor para {[l]} e {[c]}: "))
        if matriz[linha][coluna] % 2 == 0:
            par += matriz[linha][coluna]
for matriz[linha] in matriz:
    terceira_coluna += matriz[linha][2]
for coluna in range(0, 3):
    if coluna == 0:
        segunda_linha = matriz[1][coluna]
    elif matriz[1][coluna] > segunda_linha:
        segunda_linha = matriz[1][coluna]

print(f"""
{matriz[0]}
{matriz[1]}
{matriz[2]}
""")
print("-=" * 30)
print(f"A soma dos valores pares é {par}")
print(f"A soma dos valores da 3º coluna é {terceira_coluna}")
print(f"O maior valor da 2º linha é {segunda_linha}")
