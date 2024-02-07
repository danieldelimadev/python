def factorial(a, s = False):
    f = 1
    if s == True:
        for c in range(a, 0, -1):
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    for c in range(a, 0, -1):
        f *= c
    return f


print('-' * 30)    
print(factorial(5))