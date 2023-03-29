from time import sleep
from random import randint

cont = 0
guess = 0
pc = randint(0, 10)
while cont < 1:
    x = int(input("\n\033[mEm que número estou pensando?: "))
    if x == pc:
        cont += 1
    else:
        guess += 1
        print("\033[31mNúmero errado, tente novamente")
sleep(1)
print("\n\033[m...")
sleep(1)
print("...")
sleep(1)
print(f"Você fez {guess} tentativas")
sleep(1)
print("\033[32mVocê acertou!")
