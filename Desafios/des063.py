from os import system
system('cls')
print('\033[1mSEQUENCIA DE FIBONACCI\033[m')
n = int(input('\033[1mQuantos termos você quer ver? \033[m'))
print('\033[1mOs {} primeiros números da sequencia de Fibonacci são.\033[m'.format(n))
c = 0
f1 = 0
s = ' -> '
while c < n:
    if c == n - 1:
        s = '\033[1;32m FIM\033[m '
    if c == 1:
        f3 = f1
        f1 = 1
    if c > 1:
        f2 = f1 + f3
        f3 = f1
        f1 = f2
    print(end = '' '\033[1m{}\033[m{}'.format(f1, s))
    c = c + 1
