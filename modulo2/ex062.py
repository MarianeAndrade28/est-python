#Exercício 062 - Super Progressão Aritmética v3.0
print('Gerador de PA')
print('-='*12)
t1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = t1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Programa Encerrado! Número de termos mostrados: {}'.format(total))