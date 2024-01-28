from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
cpu = randint(0,2)
print('\033[1;32mJOGO: PEDRA, PAPEL E TESOURA\033[m')
print('''\033[1;36m[0] PEDRA
[1] PAPEL
[2] TESOURA\033[m''')
p1 = int(input('-> '))
print('Você jogou: {}'.format(itens[p1]))
print('Computador jogou: {}'.format(itens[cpu]))
if cpu == 0: #Cpu jogou pedra
    if p1 == 0:
        print('\033[1;36mEmpate\033[m')
    elif p1 == 1:
        print('\033[1;32mVocê ganhou.\033[m')
    elif p1 == 2:
        print('\033[1;33mVocê perdeu.\033[m')
    else:
        print('\033[1;31mJOGADA INVALIDA!.\033[m')
elif cpu == 1: #Cpu jogou papel
    if p1 == 0:
        print('\033[1;33mVocê perdeu.\033[m')
    elif p1 == 1:
        print('\033[1;36mEmpate\033[m')
    elif p1 == 2:
        print('\033[1;32mVocê ganhou.\033[m')
    else:
        print('\033[1;31mJOGADA INVALIDA!.\033[m')
elif cpu == 2: #Cpu jogou tesoura
    if p1 == 0:
        print('\033[1;32mVocê ganhou.\033[m')
    elif p1 == 1:
        print('\033[1;33mVocê perdeu.\033[m')
    elif p1 == 2:
        print('\033[1;36mEmpate\033[m')
    else:
        print('\033[1;31mJOGADA INVALIDA!.\033[m')
