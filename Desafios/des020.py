import random
a1 = input('Nome do 1° aluno: ')
a2 = input('Nome do 2° aluno: ')
a3 = input('Nome do 3° aluno: ')
a4 = input('Nome de 4° aluno: ')
lista =  [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será ')
print(lista)