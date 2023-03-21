from math import sin, cos, tan, radians

ang = int(input("enter the angle value: "))

cosseno = cos(radians(ang))
seno = sin(radians(ang))
tangente = tan(radians(ang))


print(
    f"""
The sin value is: {seno:.2f}
The cos value is: {cosseno:.2f}
The tan value is: {tangente:.2f}
"""
)
