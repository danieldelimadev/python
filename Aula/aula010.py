#nome = str(input('Qual é seu nome? '))
#if nome == 'Gustavo':
    #print('Que nome lindo você tem!')
#else:
    #print('Seu nome é feio!')
#print('Bom dia, {}!'.format(nome))

n1 = float(input('Digete a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))
m = (n1 + n2) / 2
print('Sua média foi {:.1f}'.format(m))
if m <= 5.9:
    print('Aluno reprovado')
else:
    print('Aluno aprovado')