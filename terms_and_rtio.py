x = int(input("Enter the first term: "))
y = int(input("ratio: "))
z = x + (10 - 1) * y
for i in range(x, z + y, y):
    print(i, "->", end=' ')
print("End")