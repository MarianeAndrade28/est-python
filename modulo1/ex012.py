# Exercício 012 - Calculando descontos
preco = float(input('Digite o valor do produto: R$'))
desconto = float(preco - (preco * 0.05))
print('O Valor Total é R${:.2f}\nValor com desconto de 5%: R${:.2f}'.format(preco,desconto))