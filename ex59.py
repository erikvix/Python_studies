from time import sleep

n1 = int(input("Digite o número que você quer fatorar: ") )
resultado = 1
count = 1
while count <= n1:
    print(f"{count} x", end=' ')
    resultado *= count
    count += 1

sleep(1)
print(f"= {resultado}")