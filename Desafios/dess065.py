from os import system
system('cls')
res = 's'
soma = 0
c = 0
m = 0
maior = 0
menor = 0
while res in 'Ss':
    n = int(input('\033[1mDigite um número: \033[m'))
    if c == 0:
        maior = n
        menor = n
    if c >= 0:
        res = str(input('\033[1mQuer continuar? [S/N]\033[m'))
    c = c + 1
    soma = soma + n
    if res in 'nN':
        m = soma / c
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print('\033[1mA média entre todos os valores digitados foi: {:.2f}\033[m'.format(m))
print('\033[1mO maior valor foi {} e o menor foi {}.\033[m'.format(maior, menor))
