from ex109 import *

n = float(input("Digite seu valor: $"))
print(f'O número {moeda(n)} dobrado é {dobro(n, False)}')
print(f'O metade do número {moeda(n)} é {metade(n, True)}')
print(
    f'com um aumento de 10% o número {moeda(n)} fica {aumentar(n, 10, True)}')
print(f'com desconto de 13% o número {moeda(n)} fica {desconto(n, 13 ,True)}')
