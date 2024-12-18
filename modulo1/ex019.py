#Exercício 019 - Sorteando um item da lista

import random
p = input('Primeiro aluno: ')
s = input('Segundo aluno: ')
t = input('Terceiro aluno: ')
lista = [p,s,t]
escolhido = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))

#from random import choice - Outro modo de fazer