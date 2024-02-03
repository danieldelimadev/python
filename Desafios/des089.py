boletim = []
dados = []
while True:
    m = 0
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    m = (dados[1] + dados[2]) / 2 
    dados.append(m)
    boletim.append(dados[:])
    dados.clear()
    res = str(input('Quer continuar? S/N '))
    if res in 'Nn':
        break
print('-+' * 30)
print('\033[1mnº    Nome           Média\033[m')    
for c in range(0, len(boletim)):
    print(f'{c}     {boletim[c][0]:15} {boletim[c][3]:4.1f}')
print('-+' * 30)
while True:
    esc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if esc == 999:
        break
    if esc in range(0, len(boletim)):
        print(f'Notas de {boletim[esc][0]} são {boletim[esc][1:3]}')
    else:
        print('\033[1mNão achei esse aluno.\033[m')



