import random
a1 = input('Nome do 1° aluno: ')
a2 = input('Nome do 2° aluno: ')
a3 = input('Nome do 3° aluno: ')
a4 = input('Nome do 4° aluno: ')

#---outra maneira---
#escol = random.randint(1,4)
#def nome_aluno(escol):
    #match escol:
        #case 1:
        #    return (a1) 
        #case 2:
        #    return (a2)
        #case 3:
        #    return (a3)
        #case 4:
        #    return (a4)
#print('O aluno escolhido foi {}'.format(nome_aluno(escol)))     

lista = [a1, a2, a3, a4]
sorteado = random.choice(lista)
print('O aluno sorteado foi {}'.format(sorteado))




