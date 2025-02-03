#Exercício 084 - Lista composta e análise de dados
cad = []
dados = []
pmai = pmen = 0

while True:
    cad.append(str(input('Nome: ')))
    cad.append(float(input('Peso: ')))
    if len(dados) == 0:
        pmai = pmen = cad[1]
    else:
        if cad[1] > pmai:
            pmai = cad[1]
        if cad[1] < pmen:
            pmen = cad[1]
    dados.append(cad[:])
    cad.clear()
    resp = (str(input('Deseja continuar? [S/N] ')))
    if resp in 'Nn':
        break

print('-='*30)
print(f'Os dados foram: {dados}')
print(f'Ao todo, foram cadastradas {len(dados)} pessoas.')

print(f'O maior peso foi {pmai}Kg de: ',end='')
for p in dados:
    if p[1] == pmai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi {pmen}Kg de: ', end='')
for p in dados:
    if p[1] == pmen:
        print(f'[{p[0]}]', end='')
print()