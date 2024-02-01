from os import system
system('cls')
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',  'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
cont = 0
while True:
    n = int(input('Digite um número: '))
    if  0 <= n <= 20:
        print(f'Você digitou o número \033[1m{tupla[n]}\033[m')
        while True:
            res = input('Quer ver outro número? \033[1mS/N\033[m ')
            if res in 'SsNn':
                break
        if res in 'Nn':
            break
        cont += 1
        if cont % 4 == 0:
            system('cls')
    else:
        print('Tente novamente.', end=' ')
    
        
