#Exercício 038 - Comparando números

p = int(input('Primeiro número: '))
s = int(input('Segundo número: '))

if p > s:
    print('O PRIMEIRO valor é maior.')
elif p < s:
    print('O SEGUNDO valor é maior.')
elif p == s:
    print('Os dois valores são IGUAIS.')
