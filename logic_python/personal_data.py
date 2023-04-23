people = []
person = {}

while True:
    person['name'] = str(input("Name: "))
    person['gender'] = str(input("Gender[M/F]: "))
    if person['gender'] != 'm' and person['gender'] != 'f':
        break
    person['age'] = str(input("Age: "))
    people.append(person)
    option = input("Do you want to continue [y/n]: ")
    if option == 'n':
        break

print(people)
