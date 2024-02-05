from time import sleep
c = 0
def contador(a, b, c):
    if c == 0: 
        c = 1
    if c < 0:
        c = c - +c * 2
    print('=-' * 25)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    sleep(1)
    if a < b:        
        for c in range(a, b + 1, c):
            print(f'{c} ', end ='', flush=True)
            sleep(0.3)
        print('FIM!')
    else:
        if c > 0:
            c = -c      
        for c in range(a, b - 1, c):
            print(f'{c} ', end ='', flush=True)
            sleep(0.3)
        print('FIM!')
contador(1, 10, 1)
contador(10, 0, -2)
print('=-' * 25)
print('Agora é sua vez de personalizar a contagem.')
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = int(input('Passo: ')) 
contador(a, b, c)
