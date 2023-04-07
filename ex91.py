from random import randint
from time import sleep
jogadores = {
    'jogador1': randint(0, 6),
    'jogador2': randint(0, 6),
    'jogador3': randint(0, 6),
    'jogador4': randint(0, 6),
}
ranking = {}

for k, v in jogadores.items():
    print(f"o {k} tirou {v}")
    sleep(0.5)
print('RANKING DOS JOGADORES')
for k, v in enumerate(sorted(jogadores, key=jogadores.get, reverse=True)):
    print(f' {k + 1}º lugar: {v} com {jogadores[v]}')
    sleep(0.5)
