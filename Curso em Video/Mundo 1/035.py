n1 = float(input('Valor 1: '))
n2 = float(input('Valor 2: '))
n3 = float(input('Valor 3: '))

a = (n1 + n2) > n3
b = (n1 + n3) > n2
c = (n2 + n3) > n1

if a and b and c == True:
    print('Triângulo formado com sucesso!')
else:
    print('Não é possível formar um triângulo')