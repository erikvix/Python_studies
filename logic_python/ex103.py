def leiaint(msg):
    ok = False
    val = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            val = int(n)
            ok = True
        else:
            print("Error")
        if ok:
            break
    return val


n = leiaint("Digite um número: ")
print(f" voce acabou de digitar o valor {n}")
