import random
ale = random.randint(1,5)
print('-Jogo de Adivinhaçao-')
n = int(input("Adivinhe o número de 1 a 5: "))
if n == ale:
    print('ACERTOU!!!')
else:
    print('ERROU!!!')
    print('O número erá {}'.format(ale))
