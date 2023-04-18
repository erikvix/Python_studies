list = []
i = 0
while i < 1:
    x = int(input("Enter a value: "))
    if x not in list:
        list.append(x)
    else:
        print("Number already inserted")
    x = input("Do you want to continue? [y/n]: ")
    if x == "n":
        i += 1
    elif x == "y":
        continue
else:
    print("Incorrect option")
    i += 1
print(list)
