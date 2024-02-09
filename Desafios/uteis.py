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
    return x.replace('.', ',')

def gizmo(x):
    v = f'{x:.2f}'
    return v

    
#des 109 foi modificado o des 107


#des 110
def resumo(v = 0, a = 0, r = 0):
    print('-' * 31)
    print('        RESUMO DO VALOR')
    print('-' * 31)
    print(f'{'Preço analisado:':18}', f'R${moeda(gizmo(v))}')
    print(f'{'Dobro do preço:':18}', f'R${moeda(dobro(v, True))}')
    print(f'{'Metade do preço:':18}', f'R${moeda(metade(v, True))}')
    print(f'{f'{a}% de aumento:':18}', f'R${moeda(aumentarp(v, a, True))}')
    print(f'{f'{r}% de redução:':18}', f'R${moeda(diminuirp(v, r, True))}')
    print('-' * 31)

#des112
def leiadinheiro(a):
    while True:
        p = str(input(a)).replace(',','.').strip()
        if p.isalpha() or p == '':
            print(f'\033[1;31mERRO: "{p}" é um preço inválido\033[m')
        else:
            return float(p)
        
#des113
def ReadInt(a):
    global i
    try:
        i = int(input(a))
    except (ValueError, TypeError):
        while True:
            print('\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
            i = str(input(a))
            if i.isnumeric():
                break 
    except KeyboardInterrupt:
        i = 0   
    return i


#des 115 Menu   
def menu():
    while True:
        print('\033[1m')
        print('-' * 30)
        print(f'{'Menu Principal':^30}')
        print('-' * 30)
        print('1 - Ver pessoas cadastradas\n2 - Cadastrar nova pessoa\n3 - Sair do sistema')
        print('-' * 30)
        print('\033[m')
        while True:
            opc = ReadInt('Sua opção: ')
            if opc == 1:
                print('-' * 30)
                print(f'{'Pessoas Cadastradas':^30}')
                print('-' * 30)
                AbrirArquivo('Cadastro.txt')
            elif opc == 2:
                arq = 'Cadastro.txt'
                print('-' * 30)
                print(f'{'Cadastrar Pessoa':^30}')
                print('-' * 30)
                nome = str(input('Nome: '))
                idade = ReadInt('Idade: ')
                cadastrar(arq, nome , idade)
            else:
                print('Saindo...')
                break


#des 115 Abrir o arquivo txt 
def AbrirArquivo(a):
        #ABRIR arquivo
    try:
        b = open(a, 'rt')
    except FileNotFoundError:
        #CRIAR arquivo
        b = open(a, 'wt+')
        b.close()
    else:
        #LER arquivo 
        print(b.read())
    finally:
        b.close()

    #Cadastrar pessoa no arquivo txt        
def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        b = open(arq, 'at')
    except:
        print('ERRO')
    else:   
        b.write(f'{nome:30}{idade} Anos\n')
