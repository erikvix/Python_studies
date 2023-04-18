list = ("Pencil", 1.75, "Eraser", 2.00, "Notebook", 15.90, "Pencil case", 25.00, "Protractor", 4.20,
        "Compass", 9.99, "Backpack", 120.32, "Pens", 22.30, "Book", 34.90)

print("-"*40)
print(f'{"PRICE LISTING":^40}')
print("-"*40)
for pos in range(0, len(list)):
    if pos % 2 == 0:
        print(f"{list[pos]:.<30}", end=' ')
    else:
        print(f"R$ {list[pos]:>5.2f}")
print("-"*40)
