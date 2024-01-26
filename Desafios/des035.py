print('-=' * 15)
print('Analisador de Triângulos')
print('-=' * 15)
r1 = float(input('Digite o valor da 1º reta: '))
r2 = float(input('Digite o valor da 2º reta: '))
r3 = float(input('Digite o valor da 3º reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[32mpodem formar\033[m triângulo.')
else:
    print('Os segmentos acima \033[311mnão  podem\033[m formar triângulo.')
