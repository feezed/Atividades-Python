# Biblioteca necessaria.
from random import shuffle

# Nome dos alunos.
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))

# Lista dos alunos.
alunos = [a1, a2, a3, a4]

# Print cabeçario
print('A ordem dos alunos é:')

# Randomizando a lista dos alunos.
shuffle(alunos)

# Print Lista dos alunos após ser randomizada.
print(alunos)