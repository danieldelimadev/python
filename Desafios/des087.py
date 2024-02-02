m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sp = s3c = 0
for l in range(0,3):
    for c in range(0,3):
        m[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))
        if m[l][c] % 2 == 0:
            sp += m[l][c]
        if m[l][2] != 0:
            s3c += m[l][2]
        if m[0][0] or m[1][c] > maior:
            maior = m[1][c]
print('=-' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'\033[1m{m[l][c]:^4}\033[m', end ='')
    print()
print('=-' * 30)
print(f'A soma dos valores pares é \033[1m{sp}\033[m.')
print(f'A soma dos valores da terceira coluna é \033[1m{s3c}\033[m.')
print(f'O mairo valor da seguamda linha é \033[1m{maior}\033[m')




