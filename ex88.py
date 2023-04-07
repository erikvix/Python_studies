# from random import randint

# q = int(input("Quantos jogos você quer sortear? "))


# for j in range(1, q+1):
#     for i in range(0, 6):
#         jogos = []
#         i = randint(0, 60)
#         jogos.append(i)
#     print(f"Jogo {j} : {jogos}")

# print("Boa sorte!")

from random import randint
jogos = []
mega = randint(0, 60)
q = int(input("Quantos jogos você quer sortear? "))

for i in range(1, q+1):
    jogos = []
    while len(jogos) != 6:
        i = randint(0, 60)
        if i not in jogos:
            jogos.append(i)
    print(f"Jogo {i} : {jogos}")
print("Boa sorte!")
