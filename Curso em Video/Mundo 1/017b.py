# com import

from math import hypot

oposto = float(input('Valor cateto oposto: '))
adjacente = float(input('Valor cateto adjacente: '))
hi = hypot(oposto, adjacente)
print('A hipotenusa é: {:.2f}'.format(hi))
