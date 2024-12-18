#Exercício 048 - Soma ímpares múltiplos de três
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 #cont += 1 É a mesma coisa
        soma = soma + c

print('A soma de todos os {} valores solicitados é: {}'.format(cont,soma))