#Exercício 044 - Gerenciador de Pagamentos

print('=' * 10, 'LOJAS ANDRADE', '=' *10)
preco = float(input('Preço das compras: R$'))

print('FORMAS DE PAGAMENTO:\n'
      '1 - Á vista: Dinheiro/Cheque\n'
      '2 - Á vista: Cartão\n'
      '3 - Em 2x no Cartão\n'
      '4 - Em 3x ou mais no Cartão\n')
escolha = int(input('Qual é a opção? '))

if escolha == 1:
    r = preco - (preco * 0.1)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco,r))
elif escolha == 2:
    r = preco - (preco * 0.05)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco,r))
elif escolha == 3:
    r = preco / 2
    print('Sua compra de R${:.2f} será parcelada em 2x de R${:.2f}'.format(preco,r))
elif escolha == 4:
    e = int(input('Quantas Parcelas? '))
    r = preco + (preco * 0.2)
    p = r / e
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.\n'
          'Valor Inicial: R${:.2f}'.format(e,p,preco))
else:
    print('OPÇÃO INVÁLIDA! Tente Novamente.')