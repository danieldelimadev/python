pesomaior = 0
pesomenor = 0
for c in range (1,6):
    peso = float(input('Qual o peso da {}º pessoa: Kg '.format(c)))
    if c == 1:
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print('O maior peso lido foi: {:.1f}Kg'.format(pesomaior))
print('O menor peso lido foi: {:.1f}Kg'.format(pesomenor))