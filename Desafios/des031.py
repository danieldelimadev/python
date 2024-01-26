print('     Tabela de preços \naté 200km      | acima de 200km \nR$0.50 PerKm   |  R$0.45 PerKm')
print('-' * 30)
via = int(input('Qual a distância da viagem? KM '))

if via <= 200:
    preço = via * 0.50
    print('Total a pagar: R${:.2f}'.format(preço))
else:
    preço = via * 0.45
    print('Total a pagar: R${:.2f}'.format(preço))