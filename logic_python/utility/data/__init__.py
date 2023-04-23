def dobro(n, cond=False):
    if cond == True:
        db = n + n
        m = "R$"
        return f'{m}{db}'.replace('.', ',')
    db = n + n
    return db


def metade(n, cond=False):
    if cond == True:
        mt = n / 2
        m = "R$"
        return f'{m}{mt}'.replace('.', ',')
    mt = n / 2
    return mt


def aumentar(n, d, cond=False):
    if cond == True:
        am = n+(n * d/100)
        m = "R$"
        return f'{m}{am:.2f}'.replace('.', ',')
    am = n+(n * d/100)
    return am


def desconto(n, d, cond=False):
    if cond == True:
        ds = n - (n * d/100)
        m = "R$"
        return f'{m}{ds}'.replace('.', ',')
    ds = n - (n * d/100)
    return ds


def moeda(n=0, m="R$"):
    return f'{m}{n}'.replace('.', ',')


def resum(n=0, a=0, d=0):
    db = n + n
    mt = n / 2
    am = n+(n * a/100)
    ds = n - (n * d/100)
    m = "R$"
    print("-"*30)
    print(f"{'VALUE SUMMARY':^30}")
    print("-"*30)
    print(f"Analyzed price: \t{moeda(n)}")
    print(f"Double the price: \t{dobro(n, True)}")
    print(f"Half the price: \t{metade(n, True)}")
    print(f"{a}% increase: \t\t{aumentar(n, a, True)}")
    print(f"{d}% discount: \t\t{desconto(n, d, True)}")
    print("-"*30)


def read(msg):
    ok = False
    val = 0
    while not ok:
        n = str(input(msg)).replace('.', ',').strip()
        if n.isalpha() or n == "":
            print("Incorrect number, please try again.")
        else:
            ok = True
            return float(n)
