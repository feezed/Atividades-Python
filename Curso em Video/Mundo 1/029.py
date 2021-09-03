velo = float(input('Sua velocidade: '))

if velo > 80: 
    multa = (velo - 80) * 7
    print('Você recebeu uma multa por ultrapassar a velocidade da via. \nValor de R${:.2f}'.format(multa))