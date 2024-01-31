from os import system
system('cls')
totg = totp1000  = ppmb = cont = 0
npmb = '' 
print('''============================= 
       \033[1;36mMAGAZINE LUIZA\033[m
=============================''')
while True:
    np = str(input('Nome do produto: '))
    pp = int(input('Preço do produto: R$'))
    res = str(input('Comprar outro produto? [S/N] '))
    while res not in 'SsNn':
        res = str(input('Comprar outro produto? [S/N] '))
    totg += pp
    if cont == 0 or pp < ppmb:
        ppmb = pp
        npmb = np
    if pp > 1000:
        totp1000 += 1
    if res in 'Nn':
        break
    cont += 1
print()
print(f'Total Gasto: R${totg:.2f}')
print(f'Produtos que custaram mais de R$1000: {totp1000}')
print(f'O produto mais barato foi {npmb} por R${ppmb:.2f}')
    

    