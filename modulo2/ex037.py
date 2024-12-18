#Exercício 037 - Conversor de bases numéricas

num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:\n'
      '1 - Converter para BINÁRIO\n'
      '2 - Converter para OCTAL\n'
      '3 - Converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(num,bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(num,oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(num,hex(num)[2:]))
else:
    print('Opção inválida! Tente novamente.')