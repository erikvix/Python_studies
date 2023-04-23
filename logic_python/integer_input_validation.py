def readint(msg):
    ok = False
    val = 0
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            val = int(n)
            ok = True
        else:
            print("Error")
        if ok:
            break
    return val


n = readint("Enter a number: ")
print(f"You just entered the value {n}")
