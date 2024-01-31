from os import system
system('cls')
while True:
    
    print('-' * 34)
    t = int(input('Quer ver a tabuada de qual número? '))
    print('-' * 34)
    system('cls')
    if t > 0:
        c = 1
        while c < 11:
            print(f'\033[1m{t} X {c} = {t * c}\033[m')
            c += 1
    else: 
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
