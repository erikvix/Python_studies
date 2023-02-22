from math import hypot

opposite = float(input("enter opposite width number: "))
adjacent = float(input("enter adjacent width number: "))

hypotvalue = hypot(opposite, adjacent)

print (f"""
     {opposite}² + {adjacent}² = hypot
     {opposite}² + {adjacent}² = hypot
     {opposite*opposite}  + {adjacent*adjacent} = hypot
     hypot = {opposite*opposite + adjacent*adjacent}
     hypot = √{opposite*opposite + adjacent*adjacent}
     hypot value is: {hypotvalue:.2f}
 """)