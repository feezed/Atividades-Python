frase = str(input('Frase: ')).strip().upper()

print('Aparece {} letras "A" na frase digitada.'.format(frase.count('A')))
print('A primeira letra "A" se encontra na: {} casa.'.format(frase.find('A')+1))
print('A ultima letra "A" se encontra na: {} casa.'.format(frase.rfind('A')+1))