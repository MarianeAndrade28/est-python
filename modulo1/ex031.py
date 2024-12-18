#Exercício 031 - Custo da viagem

d = float(input('Qual é a distância (Km) da sua viagem? '))
print('Você está prestes a começar uma viagem de: {}Km'.format(d))

if d > 200:
    print('O preço da sua passagem será de: R${:.2f}'.format(d * 0.45))
else:
    print('O preço da sua passagem será de: R${:.2f}'.format(d * 0.50))