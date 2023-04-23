# import the randint function from the random module
from random import randint

# generate a tuple of 5 random integers between 0 and 10
num = (randint(0, 10), randint(0, 10), randint(
    0, 10), randint(0, 10), randint(0, 10))

# print the tuple
print(num)

# print the maximum and minimum values in the tuple using the max and min functions
print(max(num), min(num))
