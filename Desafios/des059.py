from os import system
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
print('''[1] SOMAR. 
[2] MULTIPLICAR.
[3] MAIOR.
[4] NOVOS NÚMEROS.
[5] SAIR.''')
c = int(input('->'))
if c == 1:
    res = n1 + n2
    
    