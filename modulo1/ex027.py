#Exercício 027 - Primeiro e último nome de uma pessoa

n = str(input('Digite o seu nome completo: ')).strip().upper()
nome = n.split()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome)-1]))