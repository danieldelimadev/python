print('-' * 21)
print(' \033[1;36mEscola Osvaldo Cruz\033[m')
print('-' * 21)
print('Calculo de média:')
n1 = float(input('1º nota: '))
n2 = float(input('2º nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Média: {:.1f}'.format(m))
    print('\033[1;31mALUNO REPROVADO\033[m')
elif m >= 5 and m < 6.9:
    print('Média: {:.1f}'.format(m))
    print('\033[1;33mALUNO EM RECUPERAÇÃO\033[m')
else:
    print('Média: {:.1f}'.format(m))
    print('\033[1;32mALUNO APROVADO!!!\033[m')