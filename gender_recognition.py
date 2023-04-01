from time import sleep

cond = 0
gender = 0

while cond < 1:
    gender = str(input("What's your gender [M/F]: "))
    if gender == 'M':
        cond += 1
    elif gender == 'F':
        cond += 1
    else:
        print("invalid gender")
print("Wait...")
sleep(1)
if gender == 'M':
    print("You're a man!")
if gender == 'F':
    print("You're a woman!")
