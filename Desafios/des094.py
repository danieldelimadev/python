lista = []
dados = {}
#Pegar os dados
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: [M/F]'))
    if dados['sexo'] not in 'MmFf':
        print('ERRO! Por favor, digite apenas M ou F.')
        dados['sexo'] = str(input('Sexo: [M/F] '))
    dados['idade'] = int(input('Idade: '))
    r = str(input('Quer continuar? [S/N] ')) 
    if r not in 'SsNn':
        print('ERRO! Por favor, digite apenas S ou N.')
        r = str(input('Quer continuar? [S/N] '))
    lista.append(dados.copy())
    if r in 'Nn':
        break
    dados.clear()
#Calcular média
s = m = 0
for c in range(0, len(lista)):
    s += lista[c]['idade']
m = s / len(lista)
print('-=' * 50)
print(f'A) Ao todo tem {len(lista)} pessoas cadastradas.')
print(f'B) A Média de idade é {m:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end= '')
for c in range (0, len(lista)):
    if lista[c]['sexo'] in 'Ff':
        print(lista[c]['nome'], end=' ')   
print()     
print(f'D) Lista de pessoas que estão acima da média:')
for c in range(0, len(lista)):
    if lista[c]['idade'] > m:
        print(f'{lista[c]}')
print('<< ENCERRADO >>')


