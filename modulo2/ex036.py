#Exercício 036 - Aprovando empréstimo

casa = float(input('Qual o valor da casa? R$'))
s = float(input('Salário do comprador? '))
anos = int(input('Quantos anos de financiamento? '))
p = casa / (anos * 12)
minimo = s * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos, '
      'a prestação será de {:.2f}.'.format(casa,anos,p))
if p <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('EMPRÉSTIMO NEGADO!')
