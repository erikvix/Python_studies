def double(n, cond=False):
    if cond == True:
        db = n + n
        m = "R$"
        return f'{m}{db}'.replace('.', ',')
    db = n + n
    return db


def half(n, cond=False):
    if cond == True:
        mt = n / 2
        m = "R$"
        return f'{m}{mt}'.replace('.', ',')
    mt = n / 2
    return mt


def increase(n, d, cond=False):
    if cond == True:
        am = n+(n * d/100)
        m = "R$"
        return f'{m}{am:.2f}'.replace('.', ',')
    am = n+(n * d/100)
    return am


def discount(n, d, cond=False):
    if cond == True:
        ds = n - (n * d/100)
        m = "R$"
        return f'{m}{ds}'.replace('.', ',')
    ds = n - (n * d/100)
    return ds


def currency(n=0, m="R$"):
    return f'{m}{n}'.replace('.', ',')


def summary(n=0, a=0, d=0):
    db = n + n
    mt = n / 2
    am = n+(n * a/100)
    ds = n - (n * d/100)
    m = "R$"
    print("-"*30)
    print(f"{'VALUE SUMMARY':^30}")
    print("-"*30)
    print(f"Analyzed price: {currency(n)}")
    print(f"Double price: \t{double(n, True)}")
    print(f"Half price: \t{half(n, True)}")
    print(f"{a}% increase: \t{increase(n, a, True)}")
    print(f"{d}% discount: \t{discount(n, d, True)}")
    print("-"*30)
