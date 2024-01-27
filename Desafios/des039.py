from datetime import date
anoatual = date.today().year
print('[Teste de alistamento militar]')
sexo = str(input('Qual seu sexo? [M/F]: ')).strip().upper()
if sexo == 'F':
    print('Você não faz parte do alistamento obrigatório.')
    exit()
anonasc = int(input('Em que ano você nasceu? '))
idade = anoatual - anonasc
if idade < 18:
    anos = 'anos'
    if idade - 18 == -1:
        anos = 'ano'
    print('Você vai ter que se alistar ao serviço militar em {} {}.'.format(18 - idade, anos))
elif idade == 18:
    print('Parabens!!!, chegou a hora de se alistar ao serviço militar.')
else:
    anos = 'anos'
    if idade - 18 == 1:
        anos = 'ano'
    print('A idade de alistamento militar já passou a {} {}.'.format(idade - 18, anos))
