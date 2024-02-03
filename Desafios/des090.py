aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno['nome']}: '))
if aluno['média'] >= 7:
    aluno['situaçao'] = 'Aprovado'
elif 5 <= aluno['média'] < 7: 
    aluno['situaçao'] = 'Recuperação'
else:
    aluno['situaçao'] = 'Reprovado'
print(f'Nome é igual a {aluno['nome']}')
print(f'Média é igual a {aluno['média']}')
print(f'Situaçao é igual a {aluno['situaçao']}')