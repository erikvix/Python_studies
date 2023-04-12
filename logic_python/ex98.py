from time import sleep


def contador(x, y, z):
    print("-="*12)
    print(f'Contagem de {x} até {y} de {z} em {z}')
    if x < y:
        cont = x
        while cont <= y:
            print(cont)
            sleep(0.5)
            cont += z
        print('fim')
    else:
        cont = x
        while cont >= y:
            print(cont)
            sleep(0.5)
            cont -= z
        print('fim')


contador(0, 10, 1)
contador(10, 0, 2)
ini = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))
pas = int(input("Digite o passo: "))
contador(ini, fim, pas)
