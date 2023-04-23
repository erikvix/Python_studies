def voting(age):
    if age > 17 and age < 65:
        return f'At {age} years old: MANDATORY voting'
    elif age < 17:
        return f'At {age} years old: DENIED voting'
    elif age > 65:
        return f'At {age} years old: OPTIONAL voting'


birth_year = int(input("In which year were you born? "))
age = 2023 - birth_year
print(voting(age))
