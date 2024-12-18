#Exercício 061 - Progressão Aritmética v2.0
print('Gerador de PA')
print('-='*12)
t1 = int(input('Primeiro termo: '))
razao = int(input('Qual a razão?: '))
termo = t1
cont = 1
while cont <= 10:
    print('{} -> '.format(termo),end='')
    termo += razao
    cont += 1
print('FIM')