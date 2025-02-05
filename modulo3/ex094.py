#Exercício 094 - Unindo dicionários as listas
cad = list()
dados = dict()
soma = media = 0

while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Inválido! Digite apenas M ou F.')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    cad.append(dados.copy())

    while True:
        pg = str(input('Deseja continuar [S/N]? '))
        if pg in 'SsNn':
            break
        print('Inválido! Digite apenas S ou N.')
    if pg in 'Nn':
       break

print('-='*30)
print(f' A) Ao todo temos {len(cad)} pessoas cadastradas.')
media = soma / len(cad)
print(f' B) A média de idade é de {media:.2f} anos.')
print(' C) As mulheres cadastradas foram: ', end='')
for p in cad:
    if p['sexo'] in 'Ff':
        print(f'{p['nome']}, ', end='')
print()
print(' D) Lista das pessoas que estão acima da média: ')
for p in cad:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')