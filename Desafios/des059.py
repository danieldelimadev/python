from os import system
system('cls')
print('\033[1;36mEscolha 2 valores:\033[m')
n1 = int(input('\033[1mDigite o 1º número: \033[m'))
n2 = int(input('\033[1mDigite o 2º número: \033[m'))
system('cls')
c = 0
res = ''
while c != 5:
    system('cls')
    print('\033[1m|Números á calcular {} e {}|\033[m'.format(n1,n2))
    print('''[1] SOMAR 
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR''')
    print('\033[1mResposta: {}\033[m'.format(res))
    c = int(input('-> '))
    if c == 1:
        calc = n1 + n2 
        res = ('A soma é {}'.format(calc)) 
    elif c == 2:
        calc = n1 * n2 
        res = ('O produto é {}'.format(calc))
    elif c == 3:
        if n1 > n2:
            maior = n1
            res = ('O maior número é {}'.format(maior))
        else:
            maior = n2
            res = ('O maior número é {}'.format(maior))
    elif c == 4:
        n1 = int(input('\033[1mDigite o 1º número: \033[m'))
        n2 = int(input('\033[1mDigite o 2º número: \033[m'))
        res = ''               
    elif c == 5:
        print('\033[1;32mSaindo...\033[m')
    else:
        print('\033[1;31mOpção invalida\033[m')