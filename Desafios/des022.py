
nome = str(input('Digite seu nome completo: ')).strip()

print('-' * 25)
print(nome.upper())
print('-' * 25)
print(nome.lower())
print('-' * 25)
print('Seu nome tem ao todo', len(nome) - nome.count(' '), 'letras')
print('-' * 25)
print('Seu primeiro nome tem', nome.find(' '), 'letras')
