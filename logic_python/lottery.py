from random import randint
jogos = []
mega = randint(0, 60)

q = int(input("How many games do you want to generate? "))

for i in range(1, q+1):
    jogos = []
    while len(jogos) != 6:
        num = randint(0, 60)
        if num not in jogos:
            jogos.append(num)
    print(f"Game {i}: {jogos}")
print("Good luck!")
