vcasa = int(input('Qual o valor da casa? R$'))
sal = float(input('Qual seu salário mensal? R$'))
ano = int(input('Em quantos anos vai quitar o empréstimo? '))
parc = vcasa / (ano * 12)
psal = (sal * 30) / 100 
print('Para pagar uma casa de R${:.2f} em {} anos.'.format(vcasa,ano))
print('A prestação será de R${:.2f}.'.format(parc))
if parc >= psal:
    print('\033[1;31mO valor da parcela passou de 30% do salário.')
    print('Empréstimo NEGADO!!!\033[m')
else:
    print('\033[1;32mEmpréstimo ACEITO!!!\033[m')

