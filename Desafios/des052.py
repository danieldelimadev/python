for c in range(0, 10):
    num = int(input('Digite um numero: '))
    if num > 1 and num % num == 0 and num % 1 == 0 and num // 1 == 0:
        print('O número {} é primo.'.format(num))
    else:
        print('O número {} não é primo.'.format(num))
            