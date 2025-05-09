#Exercício 091 - Jogo de Dados em Python
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
rank = []

print('Valores Sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-='*30)
print('  == RANKING DOS JOGADORES ==')
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(rank):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)