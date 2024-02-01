from os import system
from random import randint
system('cls')
tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10),randint(1,10))
org = sorted(tupla)
print(f'Soteei os números: {tupla}')
print(f'O menor numero é {org[0]}')
print(f'O maior número e {org[-1]}')

