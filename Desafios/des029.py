vel = int(input('Qual velocidade o carro estava? km/h '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Sua velocidade de {}Km/h foi acima do limite de velocidade que é 80Km/h'.format(vel))
    print('Multa de {}R$'.format(multa))
else:
    print('Velocidade {}Km/h dentro do limite de velocidade'.
    format(vel))