soma = 0
y = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        y = y + 1
        soma = soma + i
print(f"A soma de {y} números é igual a {soma} ")
