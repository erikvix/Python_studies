from datetime import datetime

data = {}

data['name'] = str(input("Name: "))
data['birth year'] = int(input("Birth year: "))
data['ctps'] = int(input("Social Security Work Card (0 = doesn't have): "))
data['age'] = (datetime.now().year - data['birth year'])

if data['ctps'] != 0:
    data['hiring year'] = int(input("Year of hiring: "))
    data['salary'] = float(input("Salary R$"))
    data['retirement'] = data['age'] + 35

for key, value in data.items():
    print(f"{key} has the value of {value}")
