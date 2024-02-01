n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
tupla  = (n1, n2, n3, n4)
c9 = 0
for n in tupla:
    if n == 9:
        c9 += 1
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {c9} vezes')
if 3 in tupla:
    print(f'O valor 3 aparaceu na {tupla.index(3) + 1}ª posiçao')
else: 
    print('O número 3 não foi digitado nenhuma vez.')
print('Os valores pares digitados foram:', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')