#Exercício 056 - Analisador completo

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher20 = 0

for pess in range(1, 5):
    print('-'*5, '{}ª PESSOA'.format(pess), '-'*5,)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    somaidade += idade
    if sexo == 'M': #Verificando o homem mais velho
        if idade > maioridadehomem:
            maioridadehomem = idade
            nomevelho = nome
    elif sexo == 'F':
        if idade < 20:
            mulher20 += 1
mediaidade = somaidade / 4

print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher20))