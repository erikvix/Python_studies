média = 0
mais_velho = []
mulheres = 0
nomevelho = 0
mulheres_jovens = 0

for i in range(1, 5):
    print(f"---{i}ºPESSOA---")
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    média += idade
    sexo = str(input("Sexo [m/f]: "))

    if sexo == "m":
        mais_velho.append(idade)
        nomevelho = nome
    if sexo == "f":
        if idade <= 20:
            mulheres_jovens += 1


print(f"a média é de idades é {média / 4}")
print(
    f"O homem mais velho é {nomevelho}, com {max(mais_velho)} anos de idade")
print(f"{mulheres_jovens} mulheres tem menos de 20 anos")
