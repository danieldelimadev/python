from datetime import date
trabalhador = {}
trabalhador['nome'] = str(input('Nome: '))
ano = int(input('Data de nascimento: ')) 
trabalhador['idade'] = date.today().year - ano
trabalhador['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de Contratação: '))  
    trabalhador['salário'] = float(input('Salário: R$ '))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratação'] + 35) - date.today().year)
print('-=' * 30)
for k, v in trabalhador.items():
    print(f'  -{k} tem o valor {v}')
