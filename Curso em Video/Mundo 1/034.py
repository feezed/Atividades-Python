s = float(input('Seu salário: R$'))
superior = s + (s * 10 /100)
inferior = s + (s * 15 /100)

if s >= 1250:
    print('Novo salário R${:.2f}'.format(superior))
else:
    print('Novo salário R${:.2f}'.format(inferior))
