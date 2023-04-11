x = sum = cont = 0
x = int(input("Enter the number [Enter 999 to stop]: "))
while x != 999:
    cont += 1
    sum += x
    x = int(input("Enter the number [Enter 999 to stop]: "))
print(f"You entered {cont} numbers and the sum of them is: {sum}")
