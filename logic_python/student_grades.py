
# nome = []
# lista = []
# lista2 = []
# média = []
# # media = nota/2
# while True:
#     lista2.append(str(input("Nome: ")))
#     lista2.append(float(input("Nota 1: ")))
#     lista2.append(float(input("Nota 2: ")))
#     média.append((lista2[1] + lista2[2]) / 2)
#     lista.append(lista2[:])

#     lista2.clear()
#     op = input("Deseja continuar [y/n]: ")

#     if op == "n":
#         break
# print("-=" * 25)
# print(f"No. {'Nome'}{'Média':>20}")
# print("-" * 32)
# for pos, v in enumerate(lista):
#     print(f"{pos:<4}{v[0]:<20}{média[pos]}")
# x = str(input("Mostrar nota de qual aluno: "))
# while True:
#     print('-'*32)
#     x = str(input("Mostrar nota de qual aluno: "))
#     if x == "999":
#         break
#     if x <= len(lista) - 1:
#         print(f"Notas de {pos[0]} são {lista2[0], lista2[1]}")


lista = []
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    lista.append([nome, nota1, nota2, media])
    op = input("Deseja continuar [y/n]: ")
    if op == "n":
        break

print("-=" * 25)
print(f"No. {'Nome':<20}{'Média':>8}")
print("-" * 32)
for pos, v in enumerate(lista):
    print(f"{pos:<4}{v[0]:<20}{v[3]:>8.1f}")
while True:
    print('-'*32)
    x = str(input("Mostrar nota de qual aluno (999 interrompe): "))
    if x == "999":
        break
    if int(x) <= len(lista) - 1:
        print(
            f"Notas de {lista[int(x)][0]} são {lista[int(x)][1]}, {lista[int(x)][2]}")
