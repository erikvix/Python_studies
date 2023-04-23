#

first_num = int(input("enter the first therm "))
ratio = int(input("ratio: "))
therm = first_num
cont = 1
while cont <= 10:
    print(therm, "->", end=' ')
    therm += ratio
    cont += 1
print("end!")
