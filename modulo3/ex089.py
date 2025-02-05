#Exercício 089 - Boletim com listas compostas
cad = []

while True:
    nome = input('Nome: ')
    n1 = (float(input('Nota 1: ')))
    n2 = (float(input('Nota 2: ')))
    media = (n1 + n2) / 2
    cad.append([nome, [n1, n2], media])

    resp = input('Deseja continuar? [S/N] ')
    if resp in 'Nn':
        break

print('-='*20)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i, a in enumerate(cad):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-'*30)
    opc = int(input('Escolha o nº do aluno (999 para sair): '))
    if opc == 999:
        print('Encerrando...')
        break
    if opc <= len(cad) - 1:
        print(f'Notas de {cad[opc][0]} são {cad[opc][1]}')
        