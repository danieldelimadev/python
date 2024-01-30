from os import system
system('cls')
print('\033[1;32mPROGRESÃO ARITIMETICA\033[m')
print('    de 10 termos')
termo = int(input('Digite o 1º termo: '))
pa = int(input('Digite a razão da PA: '))
d = termo + (10 - 1) * pa
c = termo
while c < d + 1:
    print(c, end=' -> ')
    c = c + pa
print('ACABOU')