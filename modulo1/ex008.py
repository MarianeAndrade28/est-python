# Exercício 008 - Conversor de medidas
mt = float(input('Quantos metros? '))
cm = mt * 100
mm = mt * 1000
print('{} metros equivale a {:.0f} centímetros e a {:.0f} milímetros'.format(mt,cm,mm))