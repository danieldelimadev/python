hvelho = ''
idadem = 0
totm20 = 0
media = 0
for c in range(1,5):
    nome = str(input('Nome da {}º pessoa: '.format(c))).strip()
    idade = int(input('Idade da {}º pessoa: '.format(c)))
    sexo = str(input('Sexo da {}º pessoa [M/F]: '.format(c))).upper() 
    media = idade + media
    print('-' * 20)
    if sexo == 'M':
      if idade > idadem:
         idadem = idade
         hvelho = nome
    else:
       if idade < 20:
          totm20 = totm20 + 1     
print('A média de idade do grupo é: {:.1f} anos.'.format(media / 4))  
print('Com {} anos o Homem mais velho é o {}.'.format(idadem,hvelho))
print('Um total de {} mulheres tem menos de 20 anos.'.format(totm20))
