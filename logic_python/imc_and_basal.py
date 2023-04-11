# EX HEIGHT: 1.58, 1.90, 2.00

peso = float(input("What is your weight?: "))
altura = float(input("What is your height?: "))
idade = int(input("How old are you?: "))

taxa = 665 + (13.7 * peso) + (500 * altura) - (6.8 * idade)
imc = peso / (altura * altura)

print(f"You spend {taxa:.2f}calories per day.")
if imc <= 18.5:
    print("you are underweight")
    print("You need to consume +300kcal per day to gain healthy weight")

elif imc > 18.6 and imc < 25:
    print("You are in good shape")
    print("You dont need to adjust your diet")
elif imc > 25 and imc < 29.9:
    print("You are overweight")
    print("You need to practice more exercise and consume -300kcal per day to lose fat")
elif imc > 30:
    print("You are very overweight")
    print("You need to practice more exercise and consume -600kcal per day to lose fat")
