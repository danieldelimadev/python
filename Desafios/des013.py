sal = float(input('Qual o salário do funcionario? R$'))
aum = 15 * sal / 100
salf = sal + aum
print('Novo salário com 15% de aumento -> R${:.2f}'.format(salf))