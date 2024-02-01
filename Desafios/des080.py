from os import system
system('cls')
lista = []
for c in range(0,5):
    n = int(input('Digite um numero: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        p = 0
        while p < len(lista):
            if n <= lista[p]:
                lista.insert(p, n)
                break
            p += 1
print()
print(f'Os valores digitados em ordem foram {lista}')
        
    