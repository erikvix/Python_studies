i = 0
nam_list = []
we_list = []
max_nam_we = []
min_nam_we = []


while i < 1:
    nam = str(input("Nome: "))
    weight = int(input('Peso '))
    y = input("Deseja continuar [y/n]: ")
    if y == "n":
        nam_list.append(nam)
        we_list.append(weight)
        i += 1
    elif y == "y":
        nam_list.append(nam)
        we_list.append(weight)
    else:
        break

for i in max(we_list):
    max_nam_we.append(nam)
print(
    f"Ao todo, você cadastrou {len(nam)} pessoas. noem maior peso {max_nam_we}")
print(f"O maior peso foi de {max(we_list)}.")
print(f"O menor peso foi de {min(we_list)}.")
