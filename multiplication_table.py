n1 = int(input("enter a number: "))
max_number = int(input("enter max number: "))
alternativa_table = print("do you want to use alternative table?: ")
alternativa_table = input("[y/n]: ")
# asteriscos
print("*" * 18)
print("Multiplication table of {}".format(n1))
print("*" * 18)

# cálculo
if alternativa_table == "y":
    for i in range(0, +max_number, 2):
        print("{0} X {1} = {2}".format(i, n1, (i * n1)))
if alternativa_table == "n":
    for i in range(10 + 1):
        print(" {0} X {1} = {2}".format(i, n1, (i * n1)))
