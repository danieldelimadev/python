from os import system
system('cls')
cont = 1
totm18 = 0
toth = 0
totma20 = 0 
while True:
    print('-' * 26)
    print(f'   CADASTRE A {cont}º PESSOA')
    print('-' * 26)
    cont += 1
    i = int(input('Idade: '))
    s = str(input('Sexo: [M/F] '))
    while s not in 'MmFf':
        s = str(input('Sexo: [M/F] '))
    print('-' * 26)
    res = str(input('Quer continuar? [S/N] '))
    while res not in 'SsNn':
        res = str(input('Quer continuar? [S/N] '))
    if i >= 18:
        totm18 = totm18 + 1
    if s in 'Mm':
        toth = toth + 1
    if s in 'Ff':
        if i < 20:
            totma20 = totma20 + 1
    if res in 'Nn':
        break
print(f'Total de pessoas com mais de 18 anos: {totm18}')
print(f'Ao todo temos {toth} homens cadastrados')
print(f'E temos {totma20} mulheres com menos de 20 anos.')