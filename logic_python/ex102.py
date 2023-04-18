def ficha(name="<naoinformado>", gol=0):
    return f'O jogador {name} fez {gol} gol(s) no campeonato'


name = str(input("Nome: "))
gol = int(input("Gols: "))

print(ficha(name, gol))
print(ficha())
