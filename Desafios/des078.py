from os import system
system('cls')
num = []
maior = 0
menor = 0
for c in range(0,5):
    num.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0 or num[c] > maior:
        maior = num[c]
    if c == 0 or num[c] < menor:
        menor = num[c]
print('=-' * 30)
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {maior} nas posições ', end ='')
for c, v in enumerate(num):
    if v == maior:
        print(f'{c}...', end =' ')
print(f'\nO menor valor digitado foi {menor} nas posições ', end ='')
for c, v in enumerate(num):
    if v == menor:
        print(f'{c}...', end =' ')
