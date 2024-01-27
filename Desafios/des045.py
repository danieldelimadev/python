from random import randint
pc = 2
print('\033[1;32mJOGO: PEDRA, PAPEL E TESOURA\033[m')
print('\033[1;36m1- PEDRA\n2- PAPEL\n3- TESOURA\033[m')
play = int(input('-> '))
print('Computador jogou: {}'.format(pc))
if play == 3 and pc == 2:
    print('Você venceu!!!')
elif play == 2 and pc == 1:
    print('Você venceu!!!')
elif play == 1 and pc == 3:
    print('Você venceu!!!')
elif play == 3 and pc == 1:
    print('Você venceu!!!')

elif play == 3 and pc == 2:
    print('Você perdeu!!!')
elif play == 2 and pc == 1:
    print('Você perdeu!!!')
elif play == 1 and pc == 3:
    print('Você perdeu!!!')
elif play == 3 and pc == 1:
    print('Você perdeu!!!')
elif play == pc:
    print('Empate!!')
