def voto(ano):
    cond = 2023 - ano
    if cond > 17 and cond < 65:
        return f'Com {cond} anos: Voto OBRIGATORIO'
    elif cond < 17:
        return f'Com {cond} anos: Voto NEGADO'
    elif cond > 65:
        return f'Com {cond} anos: Voto OPCIONAL'


ano = int(input("Em qual ano você nasceu? "))
print(voto(ano))
