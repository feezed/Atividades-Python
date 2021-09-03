d = int(input('Distância da viagem: '))

if d <= 200:
    v = d * 0.50
else:
    v = d * 0.45

print('O valor da sua viagem é R${:.2f}'.format(v))
   
