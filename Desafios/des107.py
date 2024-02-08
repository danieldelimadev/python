import uteis

p = float(input('Qual o preço do produto: R$'))
print(f'A metade de R${p} é R${uteis.metade(p)}')
print(f'O dobro de R${p} é R${uteis.dobro(p)}')
print(f'Aumentando 10%, temos R${uteis.aumentarp(p, 10, True)}')
print(f'Diminuindo 13%, temos R${uteis.diminuirp(p, 13, True)}')