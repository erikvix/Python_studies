# ex72
numbers = ("zero", "one", "two", "three", "four", "five")
while True:
    x = int(input("Enter a number between 0 and 5: "))
    if 0 <= x <= 5:
        break
    print("Try again")
print(f"You entered the number {numbers[x]}")
