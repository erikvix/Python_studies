from time import sleep
cond = 0
while cond < 1:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    print("""
    [ 1 ] SUM
    [ 2 ] MULTIPLICATION
    [ 3 ] GREATER NUMBER
    [ 4 ] NEW NUMBERS
    [ 5 ] EXIT
    """)
    option = int(input("Qual sua opção?: "))
    if option == 1:
        cond += 1
        print(f"O número {num1} somado ao número {num2} é: {num1+num2}")
        num3 = str(input("Deseja continuar? [S/N]: "))
        if num3 == "S":
            sleep(1)
            cond -= 1
        elif num3 == "N":
            break
        else:
            print("Digite uma das opções.")
    if option == 2:
        cond += 1
        print(f"O número {num1} multiplicado ao número {num2} é: {num1*num2}")
        num3 = str(input("Deseja continuar? [S/N]: "))
        if num3 == "S":
            sleep(1)
            cond -= 1
    if option == 3:
        cond += 1
        if num1 > num2:
            print(f"O número {num1} é o maior")
        else:
            print(f"O número {num2} é o maior")
        num3 = str(input("Deseja continuar? [S/N]: "))
        if num3 == "S":
            sleep(1)
            cond += 1
    if option == 4:
        print("Fornecendo números novos...")
        sleep(1)
        cond -= 1
    if option == 5:
        sleep(1)
        print("Finalizando...")
        sleep(1)
        break

