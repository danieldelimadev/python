from random import randint
from time import sleep
l = []
def draw(list):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        list.append(randint(1,10))
        print(list[c], end=' ', flush=True)
        sleep(0.4)
    print('PRONTO!')
def sump(list):
    s = 0
    for v in list:
        if v % 2 == 0:
            s += v   
    print(f'Somando os valores pares de {list}, temos {s}')


draw(l)
sump(l)