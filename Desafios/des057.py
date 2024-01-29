s = 's'
while s not in 'MmFf': 
    s = str(input('Qual é o seu sexo? [M/F] '))
    if s in 'MmFf':
        print('\033[1;32mSexo valido.\033[m')
    else:
        print('\033[1;31mOpçao invalida.\033[m')
        print('\033[1;36mTente novamente.\033[m')