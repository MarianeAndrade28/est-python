#Exercício 073 - Tuplas com times de futebol
times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro',
'Vasco da Gama', 'EC Vitória', 'Atlético-MG', 'Fluminense',
'Grêmio', 'Juventude', 'Bragantino', 'Athletico-PR', 'Criciúma',
'Atlético-GO', 'Cuiabá')

print('-=' * 15)
print('Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são: {times[:5]}')
print(f'Os últimos 4 colocados são: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O time Bahia está na {times.index('Bahia')+1}ª posição')
