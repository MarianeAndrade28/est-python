#Exercício 045 - GAME: Pedra, Papel e Tesoura

from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
comput = randint(0,2)
print('-'*12, 'JOKENPO', '-'*12)
print('Suas Opções:\n'
      '0 - PEDRA\n'
      '1 - PAPEL\n'
      '2 - TESOURA')
jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')

print('='*20)
print('Computador jogou {}'.format(itens[comput]))
print('Jogador jogou {}'.format(itens[jogador]))
print('='*20)

if comput == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')

elif comput == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')

elif comput == 2:
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
else:
    print('JOGADA INVÁLIDA!')
