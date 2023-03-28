x = int(input("Digite o primeiro termo: "))
y = int(input("Razão: "))
z = x + (10 - 1) * y
for i in range(x, z + y, y):
    print(i, "->", end=' ')
print("ACABOU!")
