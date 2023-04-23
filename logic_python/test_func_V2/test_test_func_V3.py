from test_func_V2 import *

n = float(input("Enter a value: $"))
print(f"The number {currency(n)} doubled is {double(n, True)}")
print(f"The half of {currency(n)} is {half(n, True)}")
print(f"With a 10% increase, {currency(n)} becomes {increase(n, 10,True)}")
print(f"With a 10% discount, {currency(n)} becomes {discount(n, 10,True)}")
