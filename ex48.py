x = 0
y = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        y += 1
        x += i
print(f"the sum of {y} numbers is equal to {x} ")
