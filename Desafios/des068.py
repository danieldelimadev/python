from os import system
system('cls')
from random import randint
print('=-' * 15)
print('   \033[1;36mVAMOS \033[1;32mJOGAR \033[1;36mPAR \033[1;32mOU \033[1;36mIMPAR\033[m')
print('=-' * 15)
print('''\033[1m          ===MENU===
[1] JOGAR
[ENTER] SAIR    ''')
res = bool(input('-> '))
if res == False:
    print('\033[1mSaindo...\033[m')
cont = 0
while res:
    cpu = randint(0,10)
    print('-' * 30)
    n = int(input('Digite um valor: ')) 
    Pi = str(input('Par ou Ímpar? [P/I] '))
    print('-' * 30)
    system('cls')
    if Pi in 'Pp':
        if (n + cpu) % 2 == 0:
            print(f'Você jogou {n} e o computador {cpu}. Total de {n + cpu} DEU PAR.')
            print('Você \033[1;32mVENCEU!\033[1;0m')
            print('Vamos jogar novamente!')
            cont += 1
        else:
            print(f'Você jogou {n} e o computador {cpu}. Total de {n + cpu} DEU IMPAR.')
            print('Você \033[1;31mPERDEU!\033[1;0m')
            break
    if Pi in 'Ii':
        if (n + cpu) % 2 == 1:
            print(f'Você jogou {n} e o computador {cpu}. Total de {n + cpu} DEU IMPAR.')
            print('Você \033[1;32mVENCEU!\033[1;0m')
            print('Vamos jogar novamente!')
            cont += 1
        else:
            print(f'Você jogou {n} e o computado {cpu}. Total de {n + cpu} DEU PAR.')
            print('Você \033[1;31mPERDEU!\033[1;0m')
            break
print(f'\033[1;31mGAME OVER!\033[1;0m Você venceu {cont} vezes.\033[1m')
