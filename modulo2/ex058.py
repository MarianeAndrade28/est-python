#Exercício 058 - Jogo da Adivinhação v2.0

from random import randint
computador = randint(0,10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10. 
Será que você consegue adivinhar qual é?''')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            acertou = False
            print('Menos...Tente mais uma vez.')
        elif jogador < computador:
            acertou = False
            print('Mais...Tente mais uma vez.')
print('Acertou! Com {} tentativas. Parabéns'.format(palpites))