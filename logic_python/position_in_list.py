list = []
max_positions = []
min_positions = []
for i in range(0, 5):
    list.append(int(input(f"Enter a value for position {i}: ")))

for pos, val in enumerate(list):
    if val == max(list):
        max_positions.append(pos)
    if val == min(list):
        min_positions.append(pos)


print(f'You entered the values: {list}')
print(
    f"The highest value entered was {max(list)} at positions {max_positions}")
print(f"The lowest value entered was {min(list)} at positions {min_positions}")
