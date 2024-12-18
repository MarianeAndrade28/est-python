#Exercício 017 - Catetos e Hipotenusa
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
h = (co**2 + ca**2) ** (1/2)
print("O valor da hipotenusa é: {:.2f}".format(h))

'''import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('O valor da hipotenusa é: {:.2f}.format(hi)'''