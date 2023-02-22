from math import hypot
def calcule_hipotenusa(c, a):

    # c = float(input("Comprimento do Cateto Oposto: "))
    # a = float(input("Comprimento do Cateto adjacente: "))

    if c>0 and a>0: 
        b = hypot(c, a)

        # return (f"""
        #     A resolução do exercício fica: {c}² + {a}² = Hipotenusa
        #     {c}² + {a}² = Hipotenusa
        #     {c*c}  + {a*a} = Hipotenusa
        #     Hipotenusa = {c*c + a*a}
        #     Hipotenusa = √{c*c + a*a}
        #     O valor aproximado da Hipotenusa vai medir: {b:.2f}
        #     """)
        return b
    else:
        return -1
        # print("invalid number")
if __name__=="__main__":
    print (calcule_hipotenusa(c=2, a=3))




