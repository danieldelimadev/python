print('\033[1;32mPROGRESÃO ARITIMETICA\033[m')
print('    de 10 termos')
termo = int(input('Digite o 1º termo: '))
pa = int(input('Digite a razão da PA: '))
d = termo + (10 - 1) * pa
for c in range(termo, d + pa, pa):
    print(c, end=' -> ')
print('ACABOU')