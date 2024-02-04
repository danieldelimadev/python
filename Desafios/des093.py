jogador = {}
gols = []
jogador['nome'] = str(input('Qual o nome do jogador? '))
p = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
print('-=' * 40)
for c in range(0, p):
    gols.append(int(input(f'  Quantos gols na partida {c}? '))) 
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-=' * 40)
print(jogador)
print('-=' * 40)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 40)   
print(f'O jogador {jogador['nome']} jogou {p} partidas.')
for c in range(0, p):
    print(f'   -> Na partida {c}, fez {gols[c]} gols.')
print(f'Foi um total de {jogador['total']} gols. ')




