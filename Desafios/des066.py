from os import system
system('cls')
soma = cont = 0
while True:
    n = int(input('Digite um número (para parar 999): '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'\033[1mA soma dos {cont} valores foi {soma}!\033[m')  
