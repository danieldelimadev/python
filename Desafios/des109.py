import uteis

p = float(input('Qual o preço do produto: R$'))
print(f'A metade de R${uteis.moeda(p)} é R${uteis.metade(p, True)}')
print(f'O dobro de R${uteis.moeda(p)} é R${uteis.dobro(p, True)}')
print(f'Aumentando 10%, temos R${uteis.aumentarp(p, 10, True)}')
print(f'Diminuindo 13%, temos R${uteis.diminuirp(p, 13, True)}')