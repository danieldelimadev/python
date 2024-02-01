from os import system
t = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
c = 0
system('cls')
for p in t:
    print(f'\nNa palavra \033[1m{p.upper()}\033[m temos ', end='')
    for c in p:
        if c in 'aeiou':
            print(f'\033[1m{c}\033[m', end =' ')
            