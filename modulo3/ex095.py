#Exercício 095 - Aprimorando os Dicionários
time = []
jogador = dict()
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas.clear()
    tot = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    
    for c in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        p = str(input('Deseja continuar? [S/N] '))
        if p in 'SsNn':
            break
        print('Inválido! Digite apenas S ou N.')
    if p in 'Nn':
        break

print('-='*30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Código Inválido! Jogador não existe.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR: {time[busca]['nome']} --')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE! >>')