old = 0
new = 0

for i in range(1, 8):
    x = int(input(f"What year the {i}ª person was born? "))
    if x > 2005:
        new += 1
    else:
        old += 1

print(
    f"in all, we had {old} people of legal age and {new} minors")

# Alternative Version

# from datetime import date
# atual = date.today().year
# totmaior = 0
# totmenor = 0
# for pess in range(1, 8):
#     nasc = int(input(f"Em que ano a {pess}ª pessoa nasceu? "))
#     idade = atual - nasc
#     if idade >= 21:
#         totmaior += 1
#     else:
#         totmenor += 1
# print(
#     f"Ao todo tivemos {velho} pessoas maiores de idade, e {novo} menores de idade")
