list = []
data = []
maximum = minimum = 0
while True:
    data.append(str(input("Name: ")))
    data.append(int(input("Weight: ")))
    if len(list) == 0:
        maximum = minimum = data[1]
    else:
        if data[1] > maximum:
            maximum = data[1]
        if data[1] < minimum:
            minimum = data[1]
    list.append(data[:])
    data.clear()
    y = input("Do you wish to continue [y/n]: ")
    if y in "Nn":
        break

print("-="*30)
print(f"You have registered {len(list)} people in total")
print(f"The maximum weight was {maximum}.")
for p in list:
    if p[1] == maximum:
        print(f'{p[0]}')
    elif p[1] == minimum:
        print(f'{p[0]}')
print(f"The minimum weight was {minimum}.")
