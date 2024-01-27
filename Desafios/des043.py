print('-=' * 15)
print('      \033[1;36mCalculadora de IMC\033[m')
print('-=' * 15)
p = float(input('Qual é o seu peso? Kg '))
a = float(input('Qual é a sua altura ? M '))
imc = p / (a * a) 
print('Seu IMC: {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif imc >= 18.5 and imc <= 25: 
    print('Você está no peso ideal.')
elif imc > 25 and imc <= 30:
    print('Você está com sobrepeso.')
elif imc > 30 and imc <= 40:
    print('Você está obeso.')  
else:
    print('Você está com obesidade mórbida.')
    