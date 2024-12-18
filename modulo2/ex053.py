#Exercício 053 - Detector de Palíndromo

frase = str(input('Digite uma frase: ')).strip().upper()
p = frase.split()
junto = ''.join(p)
inverso = junto[::-1]

'''for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]'''

print('O inverso de {} é: {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO é um PALÍNDROMO!')
