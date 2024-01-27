p = float(input('Qual o preço do produto? R$'))
print('--' * 22)
print('\033[4;36mFormas de pagamento\033[m\n1: À vista no dinheiro/cheque: 10% de desconto.\n2: À vista no cartão: 5% de descoto.\n3: Em até 2x no cartão sem juros.\n4: Em até 3x ou mais no cartão: 20% de juros.')
print('--' * 22)
ch = int(input('Qual será a forma de de pagamento? '))
print('--' * 22)
if ch == 1:
    pd = p - (10 * p) / 100 
    print('O preço total com 10% de desconto fica R${:.2f}.'.format(pd))
elif ch == 2:
    pd = p -(5 * p) / 100
    print('O preço total com 5% de desconto fica R${:.2f}'.format(pd))
elif ch == 3:
    pc = p / 2
    print('Valor total {:.2f} em 2x de {:.2f}'.format(p,pc))
elif ch == 4:
    pj = (20 * p) / 100 + p 
    pc = (20 * p / 100 + p) / 3
    print('Valor total {:.2f} em 3x de {:.2f}'.format(pj,pc))
else:
    print('\033[1;31mERRO\033[m')
 