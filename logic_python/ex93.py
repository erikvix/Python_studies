
player = {}
goals = []

player['name'] = str(input("Player's name: "))
n = int(input(f"How many matches did {player['name']} play? "))
for i in range(0, n):
    goals.append(int(input(f"How many goals in match {i}? ")))
player['goals'] = goals[:]
print(player)
player['total'] = sum(goals)
for k, v in player.items():
    print(f'The {k} has the value of {v}')
print("-="*30)
print(f"Player {player['name']} played {len(player['goals'])} matches")
for i, v in enumerate(player['goals']):
    print(f' => In match {i}, scored {v} goals')
print(f"Total of {player['total']} goals")
