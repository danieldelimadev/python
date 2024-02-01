from os import system
system('cls')
num = []
c = 0
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print('\033[1mVALOR ADICIONADO\033[m')
    else:
        print('\033[1;31mVALOR NEGADO\033[m')
    while True:    
        res = input('Quer continuar? S/N ')
        if res in 'SsNn':
            break
    if res in 'Nn':
        break
    if c == 4:
        system('cls')
        c = 0
    c += 1
org = num.sort()
print(f'\033[1m{num}\033[m')
