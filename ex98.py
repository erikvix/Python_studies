from time import sleep


def contador():
    print("-="*12)
    print('Contagem de 1 até 10 de 1 em 1')
    for i in range(1, 11):
        sleep(1)
        print(i, end=' ')
    print('FIM')


contador()
