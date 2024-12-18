#Exercício 069 - Análise de Dados do Grupo
print('=-' * 20)
print('CADASTRO DE PESSOAS')
print('=-' * 20)
maior = menos20 = hom = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'F'and idade < 20:
        menos20 += 1
    if sexo == 'M':
        hom += 1
    p = ' '
    while p not in 'SN':
        p = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if p == 'N':
        break
print(f'O total de pessoas com mais de 18 anos é igual à: {maior}')
print(f'O total de homens cadastrados é igual à: {hom}')
print(f'O total de mulheres com menos de 20 anos é igual à: {menos20}')