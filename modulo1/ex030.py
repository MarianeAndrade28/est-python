#Exercício 030 - Par ou ímpar?

n = int(input('Me diga um número qualquer: '))
resultado = n % 2

if resultado == 1:
    print('O número {} é ÍMPAR.'.format(n))
else:
    print('O número {} é PAR.'.format(n))