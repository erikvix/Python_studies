import math
n1 = int(input("Digite um número inteiro: "))

print("""
Selecione as opções abaixo:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para HEXADECIMAL
[ 3 ] converter para OCTADECIMAL
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
[ 4 ] ir para o conversor de MEDIDAS
[ 5 ] ir para o conversor de TEMPERATURA
[ 6 ] ir para o conversor de MOEDAS 
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
""")
opção = input("Sua opção: ")

if opção == "1":
    print(f"o Número {n1} convertido para BINÁRIO é {bin(n1)[2:]}")
elif opção == "2":
    print(f"O número {n1} convertido para HEXADECIMAL é {hex(n1)[2:]}")
elif opção == "3":
    print(f"O número {n1} convertido para OCTADECIMAL é {oct(n1)[2:]}")
elif opção == "4":
    print("""
    Selecione as opções abaixo:
    =-=-=-=-=-=-=-=-=-=-=-=-=-=
    [ 1 ] Converter MM para CM
    [ 2 ] Converter M para CM
    [ 3 ] Converter KM para M
    -=-=-=-=-=-=-=-=-=-=-=-=-=-
    """)
    opção2 = input("Digite sua opção: ")

    if opção2 == "1":
        n2 = float(input("Digite o número em CM a ser convertido: "))
        cm = n2 / 10
        print(f"o número {n2}mm convertido para CENTÍMETROS é: {cm:.2f}cm")
    elif opção2 == "2":
        n2 = float(input("Digite o número em M a ser convetido: "))
        m = n2 * 100
        print(f"O número {n2}m convertido para CENTÍMETRO é: {m:.2f}cm")
    elif opção2 == "3":
        n2 = float(input("Digite o número em KM a ser convetido: "))
        km = n2 * 1000
        print(f"O número {n2}km convertido para Metros é: {km:.2f}m")
    else:
        print("número invalido")
elif opção == "5":
    print("""
    Selecione as opções abaixo:
    =-=-=-=-=-=-=-=-=-=-=-=-=-=
    [ 1 ] Converter CELSIUS para FAHRENHEIT
    [ 2 ] Converter FAHRENHEIT para CELSIUS
    [ 3 ] Converter CELSIUS para KEVIN
    -=-=-=-=-=-=-=-=-=-=-=-=-=-
    """)
    opção2 = input("Digite sua opção: ")
elif opção == "6":
    print("""
    Selecione as opções abaixo:
    =-=-=-=-=-=-=-=-=-=-=-=-=-=
    [ 1 ] Converter REAIS para DOLARES
    [ 2 ] Converter REAIS para EUROS
    [ 3 ] Converter REAIS para LIBRAS
    [ 4 ] Converter REAIS para 
    -=-=-=-=-=-=-=-=-=-=-=-=-=-
    """)
    opção2 = input("Digite sua opção: ")
else:
    print("VALOR INVÁLIDO")

# print(hex(n1)[2:])
# print(oct(n1)[2:])
