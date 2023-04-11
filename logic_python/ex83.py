pf = []
pa = []
ex = str(input("Digite sua expressão: "))
for i in ex:
    if i == "(":
        pf.append('(')
    elif i == ")":
        pa.append(')')
if len(pf) == len(pa):
    print('expressão correta')
else:
    print('expressão incorreta'
          )