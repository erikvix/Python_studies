matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = ter = seg = 0


for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite o valor para {[l]} e {[c]}: "))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
for matriz[l] in matriz:
    ter += matriz[l][2]
for c in range(0, 3):
    if c == 0:
        seg = matriz[1][c]
    elif matriz[1][c] > seg:
        seg = matriz[1][c]

print(f"""
{matriz[0]}
{matriz[1]}
{matriz[2]}
""")
print("-=" * 30)
print(f"A soma dos valores pares é {par}")
print(f"A soma dos valores da 3º coluna é {ter}")
print(f"O maior valor da 2º linha é {seg}")
