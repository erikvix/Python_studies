def notas(*num, sit=False):
    val = {}
    val['total'] = len(num)
    val['menor'] = min(num)
    val['maior'] = max(num)
    val['media'] = sum(num) / len(num)
    if sit == True:
        if val['media'] >= 6:
            val['situação'] = 'BOA'
        elif val['media'] >= 5:
            val['situação'] = 'RAZOÁVEL'
        else:
            val['situação'] = 'RUIM'
    return val


resp = notas(3, 8, 5, 6, sit=True)
print(resp)
