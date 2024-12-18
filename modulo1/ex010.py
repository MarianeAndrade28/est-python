# Exercício 010 - Conversor de moedas
real = float(input('Quanto você tem na carteira? R$'))
dolar = float(real / 3.27)
euro = float(real / 6.09)
print('Total em reais: R${:.2f}'.format(real))
print('Com esse valor podemos comprar US${:.2f} doláres e €{:.2f} euros'.format(dolar,euro))