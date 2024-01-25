v = int(input('Qual o preço do produto? R$'))
vf = (5 * v / 100) 
vd = v - vf
print('Com 5% de desconto fica R${:.2f1}'.format(vd))