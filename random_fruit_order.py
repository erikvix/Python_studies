import random
fruit1 = str(input("what fruit do you want to buy?: "))
fruit2 = str(input("what fruit do you want to buy?: "))
fruit3 = str(input("what fruit do you want to buy?: "))
fruit4 = str(input("what fruit do you want to buy?: "))

list = [fruit1, fruit2, fruit3, fruit4]
random.shuffle (list)

print(f"the buy order is: {list}")