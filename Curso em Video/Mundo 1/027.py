nome = str(input('Seu nome: ')).strip()
nome = nome.split()

print('Prieiro nome: {}'.format(nome[0]))
nome.reverse()
print('Último nome: {}'.format(nome[0]))