from os import system
system('cls')
n = 0
soma = 0
c = 0
while n != 999:
    n = int(input('Digite um numero: [quit=999] '))
    if n != 999:
        soma = soma + n
        c = c + 1
print('\033[1mForam digitados {} números.\033[m'.format(c))
print('\033[1mA soma entre todos esses números foi: {}\033[m'.format(soma))