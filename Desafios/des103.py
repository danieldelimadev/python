def register(n , g):
    s = ''
    if g != '1':
        s = 's'
    if n == '':
        n = '<desconhecido>'
    if g == '':
        g = 0
    print(f'O jogador {n} fez {g} gol{s} no campeonato.')


print('-' * 30)
name = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
register(name, gols)