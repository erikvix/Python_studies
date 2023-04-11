x = summ = cont = average = great = lower = 0
alt = "s"

while alt == "s":
    x = int(input("Digite um número: "))
    summ += x
    cont += 1
    average = summ / cont
    if cont == 1:
        great = lower = x
    else:
        if x > great:
            great = x
        elif x < lower:
            lower = x

    alt = str(input("Want to continue? [y/n]: "))
print(f"You entered{cont} numbers and the average of them is: {average}")
print(f"The greater number was {great} and the lowest was {lower}")
