#Exercício 060 - Cálculo do Fatorial

#Modo Simples: Utilizando o módulo
'''from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O FATORIAL de {}! é {}'.format(n, f))'''

n = int(input('''Digite um número para
calcular seu FATORIAL: '''))
c = n
f = 1
while c > 0:
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '= ', end='')
    f = f * c
    c -= 1
print('{}'.format(f))