n = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')) )
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O valor 3 aparaceu na {n.index(3) + 1}ª posiçao')
else: 
    print('O número 3 não foi digitado nenhuma vez.')
print('Os valores pares digitados foram:', end=' ')
for n in n:
    if n % 2 == 0:
        print(n, end=' ')
     