from time import sleep
from random import randint


def greatest(*num):
    greatest_num = 0
    count = 0
    print("Analyzing values...")
    sleep(1)
    for v in num:
        print(f'{v}')
        sleep(1)
        if count == 0:
            if v > greatest_num:
                greatest_num = v
        count += 1
    print(f'{len(num)} values were informed in total')
    sleep(1)
    print(f'The greatest value is {greatest_num}')


greatest(randint(1, 60), randint(1, 60), randint(
    1, 60), randint(1, 60), randint(1, 60))
