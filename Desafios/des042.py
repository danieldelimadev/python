print('-=' * 15)
print('Analisador de Triângulos')
print('-=' * 15)
r1 = float(input('Digite o valor da 1º reta: '))
r2 = float(input('Digite o valor da 2º reta: '))
r3 = float(input('Digite o valor da 3º reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[1;32mpodem formar\033[m triângulo.')
    if r1 == r2 and r2 == r3:
        print('Esse triângulo é do tipo \033[1;33mequilátero.\033[m')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Esse triângulo é do tipo \033[1;33misóceles.\033[m')
    else:
        print('Esse triângulo é do tipo \033[1;33mescaleno.\033[m')
else:
    print('Os segmentos acima \033[311mnão podem\033[m formar triângulo.')
