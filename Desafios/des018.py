from math import radians, sin, cos, tan
an = float(input('Digite o angulo que você deseja: '))
sin = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, sin))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, cos))
print('O âmgulo de {} tem a TANGENTE de {:.2f}'.format(an, tan))