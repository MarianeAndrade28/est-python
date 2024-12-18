#Exercício 015 - Aluguel de Carros
dias = int(input('Quantos dias alugados?: '))
km = float(input('Quantos km rodados?: '))

aluguel = dias * 60
rod = km * 0.15
total = aluguel + rod

print('Valor km rodados: R${:.2f}\nValor dias: R${:.2f}\nTotal a pagar: R${:.2f}'.format(rod,aluguel,total))
