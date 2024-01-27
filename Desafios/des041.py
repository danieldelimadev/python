from datetime import date
print('Confederaçao Nacional de Natação')
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print('O atleta te {} anos.'.format(idade))
if idade <= 9:
    print('Até 9 anos: Categoria Mirim')
elif idade > 9 and idade <= 14:
    print('De 9 anos até 14 anos: Categoria Infantil')
elif idade > 14 and idade <= 19:
    print('De 14 anos até 19 anos: Categoria Junior ')
elif idade == 20:
    print('De 19 anos até 20 anos: Categoria Sênior')
else:
    print('Acima de 20 anos: Categoria Master')