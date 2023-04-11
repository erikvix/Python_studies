from datetime import datetime
dados = {}


dados['nome'] = str(input("Nome: "))
dados['idade'] = int(input("Data de nascimento: "))
dados['cttps'] = int(input("Carteira de trabalho (0 = não tem): "))
dados['idade'] = (2023 - dados['idade'])
if dados['cttps'] != 0:
    dados['contratação'] = int(input("Ano de contratação: "))
    dados['salário'] = float(input("Sálario R$"))
    dados['aposentadoria'] = dados['idade'] + 35
for k, v in dados.items():
    print(f"{k} tem o valor de {v}")
