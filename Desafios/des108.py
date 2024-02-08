import uteis

p = float(input('Qual o preço do produto: R$'))
print(f'A metade de R${uteis.moeda(p)} é R${uteis.moeda(uteis.metade(p))}')
print(f'O dobro de R${uteis.moeda(p)} é R${uteis.moeda(uteis.dobro(p))}')
print(f'Aumentando 10%, temos R${uteis.moeda(uteis.aumentarp(p, 10, True))}')
print(f'Diminuindo 13%, temos R${uteis.moeda(uteis.diminuirp(p, 13, True))}')