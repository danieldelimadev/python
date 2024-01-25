print('*Saber quanto de tinta precisa para pintar uma parede*')
l = float(input('Qual é a largura da parede? '))
a = float(input('Qual é a altura da parede? '))
area = l * a
tinta = area / 2
print('Você vai precisar {:.2f}l de tinta'.format(tinta))