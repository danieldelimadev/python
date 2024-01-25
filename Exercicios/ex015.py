d = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
pdia = d * 60
pkm = km * 0.15
tot = pdia + pkm
print('O total a pagar é de R${:.2f}'.format(tot))