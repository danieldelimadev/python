lista = []
c = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    c += 1
    r = input('Quer continuar? S/N ')
    if r in 'Nn':
        break
lista.sort(reverse = True)
print('-=' * 30)
print(f'Você digitou {c} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não aparece na lista.')