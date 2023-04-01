from time import sleep

n1 = int(input("Enter a number you want to factor: ") )
result = 1
count = 1
while count <= n1:
    print(f"{count} x", end=' ')
    result *= count
    count += 1

sleep(1)
print(f"= {result}")