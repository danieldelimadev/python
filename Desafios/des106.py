def lin(a):
    print('\033[1;30;42m', end='')
    size = len(a) + 4
    print('~' * size)
    print(f'  {a}')
    print('~' * size)
    print('\033[m', end='')

def pyHELP(a):
    print('\033[1;30;42m', end='')
    print(f'{help(a)}')
    print('\033[m')

while True:
    lin('SISTEMA DE AJUDA pyHELP')
    ans = (str(input('\033[mFunção ou Biblioteca > ')))
    if ans.upper() == 'FIM':
        break
    else:
        pyHELP(ans)
lin('Até Logo')