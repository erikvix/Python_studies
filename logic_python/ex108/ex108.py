def dobro(n):
    db = n + n
    return db


def metade(n):
    mt = n / 2
    return mt


def aumentar(n):
    am = n * 1.10
    return am


def desconto(n):
    ds = n - (n * 0.10)
    return ds


def moeda(n=0, m="R$"):
    return f'{m}{n}'.replace('.', ',')
