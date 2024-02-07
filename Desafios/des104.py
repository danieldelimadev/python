def ReadInt(a):
    global n
    n = str(input(a)).strip()
    if n.isnumeric():
        n == int(n)
    else:
        while True:
            print('\033[1;31mERRO! Digite um número inteiro\033[m')
            n = str(input(a)).strip()
            if n.isnumeric():
                break
    return n 


n = ReadInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')