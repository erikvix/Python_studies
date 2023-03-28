média = 0
mais_velho = []
mulheres = 0
nomevelho = 0

for i in range(1, 5):
    print(f"---{i}ºPESSOA---")
    # nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [m/f]: "))

    if sexo == "m":
        mais_velho.append(idade)
        # nomevelho = nome


print(f"a média é {média / 4}")
print(max(mais_velho))
