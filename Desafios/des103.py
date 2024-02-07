def register(n = '<desconhecido>', g = 0):
    s = ''
    if g != 1:
        s = 's'
    print(f'O jogador {n} fez {g} gol{s} no campeonato.')


print('-' * 30)
name = str(input('Nome do jogador: ')).strip()
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if name == '':
    register(g = gols)
else:
    register(name, gols)
