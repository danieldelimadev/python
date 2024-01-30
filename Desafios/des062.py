from os import system
system('cls')
print('\033[1;32mPROGRESÃO ARITIMETICA\033[m')
print('\033[1m    de 10 termos\033[m')
termo = int(input('\033[1mDigite o 1º termo: \033[m'))
pa = int(input('\033[1mDigite a razão da PA: \033[m'))
d = termo + (10 - 1) * pa
c = termo
res = 's'
s = ' -> '
while res in 'Ss':
    while c < d + 1:
        if c == d:
            s = ''
        print('\033[0;36m{}\033[m'.format(c), end='' '\033[1m{}\033[m'.format(s))
        s = ' -> '
        c = c + pa
    print()
    res = str(input('\033[1mQuer ver mais alguns termos? [S/N] \033[m'))
    if res in 'Ss':
        quant = int(input('\033[1mQuantos? \033[m')) 
        limpatela = str(input('\033[1;32mQuer limpar a tela? [S/N]\033[m')) 
        if limpatela in 'Ss':
            system('cls')
        quant = c + (quant - 1) * pa
        while c < quant + 1:
            if c == quant:
                s = ''
            print('\033[0;36m{}\033[m'.format(c), end='' '\033[1m{}\033[m'.format(s))
            s = ' -> '
            c = c + pa 
print('\033[1;36mSAINDO...\033[m')