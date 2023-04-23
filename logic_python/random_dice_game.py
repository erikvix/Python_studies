from random import randint
from time import sleep

players = {
    'player1': randint(0, 6),
    'player2': randint(0, 6),
    'player3': randint(0, 6),
    'player4': randint(0, 6),
}
ranking = {}

for k, v in players.items():
    print(f"{k} rolled {v}")
    sleep(0.5)

print('RANKING OF PLAYERS')
for k, v in enumerate(sorted(players, key=players.get, reverse=True)):
    print(f'{k + 1}º place: {v} with {players[v]}')
    sleep(0.5)
