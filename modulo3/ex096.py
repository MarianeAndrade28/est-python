#Exercício 096 - Função que calcula área
def area(larg, compr):
    a = larg * compr
    print(f'A área de um {larg}x{compr} é de {a}m²') 

#Programa Principal
print('Controle de Terreno')
print('-'*30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)