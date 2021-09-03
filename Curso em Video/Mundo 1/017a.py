# sem import

Oposto =  float(input('Cateto oposto: '))
Adjacente = float(input('Cateto adjacente: '))

hipotenusa = (Oposto ** 2 + Adjacente ** 2) **(1/2)

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))