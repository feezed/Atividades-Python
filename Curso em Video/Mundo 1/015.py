dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodou?'))

p = (dias * 60) + (km * 0.15)

print('O valor a pagar é: R${:.2f}'.format(p))
