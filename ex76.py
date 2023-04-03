teste = ("2")
n9 = 0
n1 = (int(input("porraniuma: ")),
      int(input("porraniuma: ")),
      int(input("porraniuma: ")),
      int(input("porraniuma: ")))
print(n1)
print(f" O valor 9 apareceu {n1.count(9)} vezes")
print(f"o valor 3 apareceu na {n1.index(3)}ª posição")
print(f" os valores pares digitados foram ")
for n in n1:
    if n % 2 == 0:
        print(n)
