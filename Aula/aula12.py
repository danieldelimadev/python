nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Tiaga ' or nome == 'Paulo':
    print('Seu nome é popular no Brasil.')
elif nome in 'Ana Cláudia Fernanda Bruna':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}!'.format(nome))