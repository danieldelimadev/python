pessoas = []
dados = []
pesados = []
leves = []
while True: 
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: Kg ')))
    pessoas.append(dados[:])
    dados.clear()
    while True:
        r = str(input('Quer continuar? [S/N]'))
        if r in 'SsNn':
            break
    if r in 'Nn':
        break
for p, v in enumerate(pessoas):
    if p == 0 or v[1] >= mpeso:
        mpeso = v[1]
    if p == 0 or v[1] <= lpeso:
        lpeso = v[1]
for p, v in enumerate(pessoas):
    if mpeso == v[1]:
        pesados.append(v[0])
    if lpeso == v[1]:
        leves.append(v[0])
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {mpeso:.1f}Kg. Peso de {pesados}')
print(f'O menor peso foi de {lpeso:.1f}Kg. Peso de {leves}')

