from time import sleep
from random import randint


def maior(*num):
    mai = 0
    cont = 0
    print("Analisando os valores...")
    sleep(1)
    for v in num:
        print(f'{v}')
        sleep(1)
        if cont == 0:
            if v > mai:
                mai = v
    print(f'foram informados, {len(num)} no total')
    sleep(1)
    print(f'O maior valor é {mai}')


maior(randint(1, 60), randint(1, 60), randint(
    1, 60), randint(1, 60), randint(1, 60))
