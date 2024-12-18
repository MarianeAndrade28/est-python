#Exercício 028 - Jogo de adivinhação v.1.0

from random import randint
from time import sleep # Faz o computador efetuar uma pausa
computador = randint(0,5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer.')
else:
    print('GANHEI! Eu pensei no número {} e não no {}.'.format(computador,jogador))
