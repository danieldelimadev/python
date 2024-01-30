from random import randint
from os import system
system('cls')
cpu = randint(0,10)
resp = 11
cont = 1
print('-' * 30)
print('''   \033[1mTente adivinhar o número
    que o computador está\033[m      
         \033[1;36m"pensando"\033[m''')
print('-' * 30)
print('\033[1m|Adivinhe um número de 0 a 10|\033[m')
while resp != cpu:
    resp = int(input('-> '))
    if resp > cpu:
        print('\033[1;31mMenos...!!!\033[m')
        cont += 1
    if resp < cpu:
        print('\033[1;31mMais...!!!\033[m')
        cont += 1
print('\033[1;32mACERTOU!!!\033[m')
print('Número de tentativa \033[1m{}\033[m.'.format(cont))