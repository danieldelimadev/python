n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
if n1 > n2:
    print('\033[1;36mO 1º valor é maior.\033[m')
elif n2 > n1:
    print('\033[1;36mO 2º valor é maior.\033[m')
else:
    print('\033[1;33mNão existe valor maior, os dois são iguais.\033[m')