def ReadInt(a):
    global i
    try:
        i = int(input(a))
    except (ValueError, TypeError):
        while True:
            print('\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
            i = str(input(a))
            if i.isnumeric():
                break 
    except KeyboardInterrupt:
        i = 0   
    return i


def ReadFloat(a):
    global f
    try:
        f = float(input(a))
    except (ValueError, TypeError):
        while True:
            print('\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
            f = str(input(a))
            if f.isdecimal:
                break 
    except KeyboardInterrupt:
        print('\033[1;31mUsuario preferiu não digitar esse número>\033[m')
        f = 0   
    return f



i = ReadInt('Digite um número inteiro: ')
f = ReadFloat('Digite um número real: ')
print(f'O valor inteiro foi {i} e o real foi {f}')