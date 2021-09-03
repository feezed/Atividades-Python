from random import randint
from time import sleep

pc = randint(0,5)
humano = int(input('Acerte o número que o computado escolheu de 0 a 5: '))

print('Processando...')
sleep(3)

if humano == pc:
    print('YOU WIN!')
else:
    print('YOU LOSE!')
