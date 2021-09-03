# manipulando texto, sem mecher na string.

nome = str(input('Seu nome completo: ')).strip() # .strip() remove os espaçõs do inicio e do final.

print('O nome é {}'.format(nome))
print(nome.upper()) # str maiúscula.
print(nome.lower()) # str minúscula.

print('Seu nome tem {} letras.'.format(len(nome) - nome.count(" ")))

nome = nome.split() # remove os espações e divide a str.
nome = nome[0] # separa a primeira str que foi divida com o split().
print(len(nome)) # conta quantos caracteres tem na str.

