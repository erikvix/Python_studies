valor = float(input("Qual o valor da casa? $"))
salario = float(input("Qual o seu salário atual? $"))
tempo = float(input("Quantos anos de financiamento? "))

financiamento = valor / (tempo * 12)
minimo = salario * 30/100

print(
    f"Com o valor de R${valor:.2f} e o salário de R${salario} você pagará R${financiamento:.2f} por mês para financiar essa casa")

if financiamento <= minimo:
    print("Empréstimo concedido!")
else:
    print("Empréstimo NEGADO")
