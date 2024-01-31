from os import system

system('cls')
print('=' * 21)
print('{:^28}'.format('\033[1mATM\033[m'))
print('=' * 21)
valor = int(input('Qual valor você quer sacar? \033[1mR$ \033[m'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de \033[1m{totced}\033[m cédulas de \033[1mR${ced}\033[m')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 21)
print('Tchau.')