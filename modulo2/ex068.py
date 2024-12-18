#Exercício 068 - Jogo de Par ou Ímpar
print('=-'*30)
print('VAMOR JOGAR PAR OU ÍMPAR')
print('=-'*30)
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    compt = randint(0,11)
    total = jogador + compt
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {compt}. Total de {total} -> ',end='')
    print('deu PAR'if total % 2 == 0 else 'deu ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('=-' * 30)
    print('Vamos jogar novamente...')
print('=-' * 30)
print(f'Número de Vitórias: {v} vezes. GAME OVER!')