num = int(input('Digite qualquer número inteiro: '))
print('-='*20)
print('Digite 1 para binario\nDigite 2 para octal\nDigite 3 para hexadecimal')
ch = int(input('-> '))
print('-='*20)
if ch == 1:
    print('{} em Binario fica {}'.format(num, bin(num)))
elif ch == 2:
    print('{} em Octal fica {}'.format(num, oct(num)))
elif ch == 3:
    print('{} em Hexadecimal fica {}'.format(num, hex(num)))
else:
    print('\033[31mERRO')
