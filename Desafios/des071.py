from os import system

system('cls')
print('=' * 21)
print('\033[1m         ATM\033[m')
print('=' * 21)
valor = int(input('Qual valor você quer sacar? R$'))
tot = 0
v50 = valor / 50
v20 = valor / 20
v10 = valor / 10
v1= valor / 1
print(v1, v10, v20, v50)
if valor >= 100:
    tot = valor / 50
    print(f'Total de {tot:.0f} cédulas de R$50')
