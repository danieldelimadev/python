from random import randint
from time import sleep
jogo = []
jogadas = []
print('\033[1m-' * 32)
print('{:^42}'.format('\033[1;32mBET\033[1;m'))
print('-\033[m' * 32)
q = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 3, f'SORTEANDO {q} JOGOS','-=' * 3)
for c in range(0, q):
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in jogadas:
            jogadas.append(n)
            cont += 1
        if cont == 6:
            break
    jogo.append(jogadas[:])
    jogadas.clear()
cont = 1
for p in range(0, q):
    jogo[p].sort()
    print(f'Jogo {cont}: {jogo[p]}')
    cont += 1
    sleep(0.7) 
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
