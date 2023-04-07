list = {}

list['nome'] = str(input("Nome: "))
list['média'] = float(input(f"Média de {list['nome']}: "))

if list['média'] >= 7:
    list['status'] = 'Aprovado'
elif 5 <= list['média'] < 7:
    list['status'] = 'Recuperação'
else:
    list['status'] = 'Reprovado'

for k, v in list.items():
    print(f"{k} é {v}")
