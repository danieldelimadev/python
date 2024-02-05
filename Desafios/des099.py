from time import sleep
def analyse(*n):
    print('=-' * 30)
    print('Analisando valores passados...')
    sleep(0.8)
    for c in range (0, len(n)):
        print(f'{n[c]} ', end = '', flush= True)
        sleep(0.5)
    print(f'Foram informados {len(n)} valores ao todo.')
    if len(n) > 0:
        print(f'O maior valor informado foi {max(n)}.') 
analyse(2, 9, 4 , 5, 7, 1)
analyse(4, 7, 0)
analyse(1, 2)
analyse()
analyse(-1, -2, -3)