from time import sleep

cond = 0
x = 0

while cond < 1:
    x = str(input("Qual seu sexo [M/F]: "))
    if x == 'M':
        cond += 1
    elif x == 'F':
        cond += 1
    else:
        print("Sexo inválido")
print("Aguarde...")
sleep(1)
if x == 'M':
    print("Você é um homem!")
if x == 'F':
    print("Você é um mulher!")
