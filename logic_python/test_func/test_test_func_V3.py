from test_func import *

n = float(input("Enter a value: $"))
print(f"The number {currency(n)} doubled is {currency(double(n))}")
print(f"The half of {currency(n)} is {currency(half(n))}")
print(f"With a 10% increase, {currency(n)} becomes {currency(increase(n))}")
print(f"With a 10% discount, {currency(n)} becomes {currency(discount(n))}")
