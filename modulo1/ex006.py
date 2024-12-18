# Exercício 006 - Dobro, triplo e raiz quadrada
x = int(input('Digite um número: '))
d = x * 2
t = x * 3
r = x ** (1/2)
print('Você escolheu: {}\nO dobro desse número é: {}\nO triplo é: {}\nE a raíz quadrada é: {:.2f}'.format(x,d,t,r))

# O comando pow(n, (1/2)) também cálcula a raiz quadrada