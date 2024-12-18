#Exercício 059 - Criando um Menu de opções
from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    1) Somar
    2) Multiplicar
    3) Maior
    4) Novos números
    5) Sair do Programa''')
    opcao = int(input('Qual é a sua opção? '))

    if opcao == 1:
        r = v1 + v2
        print('A soma entre {} + {} é igual à {}'.format(v1,v2,r))
    elif opcao == 2:
        print('A operação {} x {} é igual à {}'.format(v1,v2,(v1*v2)))
    elif opcao == 3:
        if v1 > v2:
            print('Entre {} e {}, o MAIOR é {}'.format(v1,v2,v1))
        else:
            print('Entre {} e {} o MAIOR é: {}'.format(v1,v2,v2))
    elif opcao == 4:
        print('Informe os números novamente:')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida! Tente novamente.')
    print('=-='*10)
    sleep(2)
print('Programa Encerrado com Sucesso!')