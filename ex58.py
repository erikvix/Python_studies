from time import sleep
cond = 0
while cond < 1:
    x = int(input("Digite um número: "))
    y = int(input("Digite outro número: "))

    print("""
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] EXIT
    """)
    z = int(input("Qual sua opção?: "))
    if z == 1:
        cond += 1
        print(f"O número {x} somado ao número {y} é: {x+y}")
        o = str(input("Deseja continuar? [S/N]: "))
        if o == "S":
            sleep(1)
            cond -= 1
        elif o == "N":
            break
        else:
            print("Digite uma das opções.")
    if z == 2:
        cond += 1
        print(f"O número {x} multiplicado ao número {y} é: {x*y}")
        o = str(input("Deseja continuar? [S/N]: "))
        if o == "S":
            sleep(1)
            cond -= 1
    if z == 3:
        cond += 1
        if x > y:
            print(f"O número {x} é o maior")
        else:
            print(f"O número {y} é o maior")
        o = str(input("Deseja continuar? [S/N]: "))
        if o == "S":
            sleep(1)
            cond += 1
    if z == 4:
        print("Fornecendo números novos...")
        sleep(1)
        cond -= 1
    if z == 5:
        sleep(1)
        print("Finalizando...")
        sleep(1)
        break

