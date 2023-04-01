# Fibonnaci

therm = int(input("Enter the number: "))

cont = 0
t1 = 0
t2 = 1
t3 = 0
print(f"{t1} -> {t2}", end=' ')
while cont <= therm:
    cont += 1
    t3 = t1 + t2
    print(f"-> {t3}", end=' ')
    t1 = t2
    t2 = t3

# 1,1,2,3,5,8,13,21
# n+n+m+n,
