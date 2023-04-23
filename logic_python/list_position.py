list = []
max_pos = []
min_pos = []
for i in range(0, 5):
    list.append(int(input(f"Enter a value for position {i}: ")))

for pos, val in enumerate(list):
    if val == max(list):
        max_pos.append(pos)
    if val == min(list):
        min_pos.append(pos)

print(f'You entered the values {list}')
print(f"The maximum value entered was {max(list)} in the positions {max_pos}")
print(f"The minimum value entered was {min(list)} in the positions {min_pos}")
