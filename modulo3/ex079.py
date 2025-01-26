#Exercício 079 - Valores únicos em uma lista
num = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não adicionado.')
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break

print('-='*30)
num.sort()
print(f'Você digitou os seguintes valores: {num}')