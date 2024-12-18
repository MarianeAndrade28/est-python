#Exercício 050 - Soma dos pares
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um {} valor: '.format(c)))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('Você informou {} números PARES. A SOMA é: {}'.format(cont,soma))