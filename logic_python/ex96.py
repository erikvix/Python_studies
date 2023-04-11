def i():
    print("Controle de terrenos")
    print("-"*18)


def area(x, y):
    print(f"A área de um terreno de {x}x{y}m é de {x*y}m²")


i()
x = float(input("LARGURA (m): "))
y = float(input("COMPRIMENTO (m): "))
area(x, y)
