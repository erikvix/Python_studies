p = []
g = {}
while True:
    p['nome'] = str(input("Nome: "))
    p['sexo'] = str(input("Sexo[M/F]: "))
    if p['sexo'] != 'm' and p['sexo'] != 'f':
        break
    p['idade'] = str(input("Idade: "))
    g.append(p)
    op = input("Quer continue [y/n]: ")
    if op == 'n':
        break
print(g)


# sex = str(input("Sexo[M/F]: "))
#     if sex != 'm' and sex != 'f':
#         print("SEXO INVÁLIDO")
#     else:
#         p['sex'] = sex
