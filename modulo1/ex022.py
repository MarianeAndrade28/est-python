#Exercício 022 - Analisador de Textos
nome = str(input('Digite seu nome completo: '))

prim = nome.split()[0]
let = len(prim)

print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(prim,let))