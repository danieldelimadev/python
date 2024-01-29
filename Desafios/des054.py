from datetime import date
totu = 0
totl = 0
for c in range(1, 8):
    ano = int(input('Ano de nascimento da {}º pessoa: '.format(c)))
    idade = date.today().year - ano
    if idade >= 21:
        totu = totu + 1
    else:
        totl = totl + 1
print('Um total de {} pessoas são maiores de idade.'.format(totu))
print('Um total de {} pessoas são menores de idade.'.format(totl))