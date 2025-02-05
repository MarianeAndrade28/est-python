#Exercício 088 - Palpites para a Mega Sena
from random import randint
from time import sleep
lista = []
jogos = []

print('-'*30)
print('      JOGUE NA MEGA SENA    ')
print('-'*30)
sort = int(input('Quantos jogos você quer sortear?'))
tot = 0
while tot <= sort:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f'SORTEANDO {sort} JOGOS', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1.2)
print('-='*5, '< BOA SORTE! >', '-='*5)
