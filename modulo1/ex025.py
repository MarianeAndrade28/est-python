#Exercício 025 - Procurando uma string dentro da outra

nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
