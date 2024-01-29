s = 0
for c in range(1,7):
    num =int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        s = s + num
print('A soma dos valores pares é {}.'.format(s))
