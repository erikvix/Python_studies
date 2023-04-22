from ex108 import *

n = float(input("Digite seu valor: $"))
print(f'O número {moeda(n)} dobrado é {moeda(dobro(n))}')
print(f'O metade do número {moeda(n)} é {moeda(metade(n))}')
print(f'com um aumento de 10% o número {moeda(n)} fica {moeda(aumentar(n))}')
print(f'com desconto de 10% o número {moeda(n)} fica {moeda(desconto(n))}')
