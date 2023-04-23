def double(n):
    db = n + n
    return db


def half(n):
    mt = n / 2
    return mt


def increase(n):
    am = n * 1.10
    return am


def discount(n):
    ds = n - (n * 0.10)
    return ds


def currency(n=0, m="$"):
    return f'{m}{n:,.2f}'
