from random import randint
cpu = randint(0,10)
resp = 11
cont = 0
print('-' * 30)
print('''   \033[1mTente adivinhar o número
    que o computador está\033[m      
         \033[1;36m"pensando"\033[m''')
print('-' * 30)
print('\033[1m|Adivinhe um número de 0 a 10|\033[m')
while resp != cpu:
    resp = int(input('-> '))
    if resp != cpu:
        print('\033[1;31mERROU!!!\033[m')
        cont += 1
cont += 1
print('\033[1;32mACERTOU!!!\033[m')
print('Número de tentativa {}.'.format(cont))