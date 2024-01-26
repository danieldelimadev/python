import math
sal = float(input('Qual o seu sálario? R$'))
if sal >= 1250:
    nsal = (10 * sal) / 100 + sal
    print('Novo salário com aumento de 10% fica R${:.2f}'.format(nsal))
else:
    nsal = (15 * sal) /100 + sal
    print('Novo salário com 15% de aumento fica R${:.2f}'.format(nsal))