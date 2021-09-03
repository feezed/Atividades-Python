from math import cos, sin, tan, radians

angulo = float(input('Ângulo: '))

cos = cos(radians(angulo))
print('O ângulo {} tem o COSSENO de {:.2f}'.format(angulo, cos))

sen = sin(radians(angulo))
print('O ângulo {} tem o SENO de {:.2f}'.format(angulo, sen))

tan = tan(radians(angulo))
print('O ângulo {} tem a TANGENTE de {:.2f}'.format(angulo, tan))