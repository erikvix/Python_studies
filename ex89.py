
nome = []
lista = []
lista2 = []
média = []
# media = nota/2
while True:
    lista2.append(str(input("Nome: ")))
    lista2.append(float(input("Nota 1: ")))
    lista2.append(float(input("Nota 2: ")))
    média.append((lista2[1] + lista2[2]) / 2)
    lista.append(lista2[:])

    lista2.clear()
    op = input("Deseja continuar [y/n]: ")

    if op == "n":
        break
print("-=" * 25)
print(f"No. {'Nome'}{'Média':>20}")
print("-" * 32)
# for pos, v in enumerate(lista):
#     print(f"{pos:<4}{v[0]:<20}{média[pos]}")
# # x = str(input("Mostrar nota de qual aluno: "))
# # while True:
# #     print('-'*32)
# #     x = str(input("Mostrar nota de qual aluno: "))
# #     if x == 999:
# #         break
# #     if x <= len(lista) - 1:
# print(f"Notas de {pos[0]} são {lista2[0], lista2[1]}")
