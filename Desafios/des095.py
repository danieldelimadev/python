jogador = {}
time = []
gols = []
while True: 
    jogador['nome'] = str(input('Qual o nome do jogador? '))
    p = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    for c in range(0, p):
        gols.append(int(input(f'  Quantos gols na partida {c + 1}? '))) 
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols) 
    time.append(jogador.copy())
    jogador.clear()
    gols.clear()
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break 
print('-=' * 30)  
print(f'{'cod nome':20}', f'{'gols':15}', 'total')
print('-' * 42)
for c in range(0, len(time)):
    print(f' {c}  {time[c]['nome']:17}{str(time[c]['gols']):15} {time[c]['total']} ')
print('-' * 42)
while True:
    l = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if l == 999:
        break
    if l > len(time) or l < 0:
        print(f'ERRO! Não existe jogador com código {l}!')
        l = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    print(f'-- LEVANTAMENTO DO JOGADOR {time[l]['nome']}:')
    for c, v in enumerate(time[l]['gols']):
        print(f'   No jogo {c + 1} fez {v} gols.')