average = 0
oldest = []
old_name = 0
young_woman = 0

for i in range(1, 5):
    print(f"---{i}ºPERSON---")
    name = str(input("Name: "))
    age = int(input("Age: "))
    average += age
    gender = str(input("Gender [m/f]: "))

    if gender == "m":
        oldest.append(age)
        old_name = name
    if gender == "f":
        if age <= 20:
            young_woman += 1


print(f"the average age is: {average / 4}")
print(
    f"O homem mais velho é {old_name}, com {max(oldest)} anos de idade")
print(f"{young_woman} mulheres tem menos de 20 anos")
