#Exercício 093 - Cadastro de jogador de futebol
jogador = dict()
partidas = []

jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?' ))
for c in range(0,tot):
    partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} temo valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {tot} partidas')
for i, v in enumerate(partidas):
    print(f'-- Na partida {i+1}, o jogador fez {v} gols.')
print(f'Total de gols: {jogador["total"]}')