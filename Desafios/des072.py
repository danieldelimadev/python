tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',  'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número entre 0 e 20: '))
if 0 <= n <= 20:
    print(f'Você digitou o número \033[1m{tupla[n]}\033[m')
else:
    while True:
        n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
        if n >= 0 and n <= 20: 
            print(f'Você digitou o número \033[1m{tupla[n]}\033[m')
            break
