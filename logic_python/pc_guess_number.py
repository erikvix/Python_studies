from time import sleep
from random import randint

cont = 0
guess = 0
pc = randint(0, 10)
while cont < 1:
    numb = int(input("\n\033[mWhat number am i thinking?: "))
    if numb == pc:
        cont += 1
    else:
        guess += 1
        print("\033[31mWrong number, try again")
sleep(1)
print("\n\033[m...")
sleep(1)
print("...")
sleep(1)
print(f"You made {guess} attempts")
sleep(1)
print("\033[32mYou got it!")
