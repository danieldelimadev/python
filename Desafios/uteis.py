#Des 107
def metade(x, sit = False):
    m = x / 2
    if sit == True:
        return f'{m:.2f}'
    else:
        return m

def dobro(x, sit = False):
    d = x * 2
    if sit == True:
        return f'{d:.2f}'
    else:
        return d

def aumentarp(x, a, sit = False):
    a = (x * 10) / 100 + x
    if sit == True:
        return f'{a:.2f}'
    else:
        return a

def diminuirp(x, d = 0, sit = False):
    d = x - (x * d / 100) 
    if sit == True:
        return f'{d:.2f}'
    else:
        return d

#des 108
def moeda(x):
    return f'{x:.2f}'


#des 109 foi modificado o des 107


#des 110
def resumo(v = 0, a = 0, r = 0):
    print('-' * 31)
    print('        RESUMO DO VALOR')
    print('-' * 31)
    print(f'{'Preço analisado:':18}', f'R${v:.2f}')
    print(f'{'Dobro do preço:':18}', f'R${dobro(v, True)}')
    print(f'{'Metade do preço:':18}', f'R${metade(v, True)}')
    print(f'{f'{a} de aumento:':18}', f'R${aumentarp(v, a, True)}')
    print(f'{f'{r} de redução:':18}', f'R${diminuirp(v, r, True)}')
    print('-' * 31)

#des112
def leiadinheiro(a):
    p = str(input(a)).strip()
    if p.isnumeric():
        p = float(p)
    elif p.isalnum():
        
    else:
        while True:
            print(f'\033[1;31mERRO: "{p}" é um preço inválido!\033[m')
            print(type(p))
            p = str(input(a)).strip()
            if p.isnumeric():
                break
    return p     
    
