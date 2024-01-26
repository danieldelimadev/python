vcasa = int(input('Qual o valor da casa? '))
sal = float(input('Qual seu salário mensal? '))
ano = int(input('Em quantos anos vai quitar o empréstimo? '))
parc = vcasa / (ano * 12)
psal = (sal * 30) / 100 
if parc >= psal:
    print('Empréstimo negado')
else:
    print('Empréstimo aceito')

