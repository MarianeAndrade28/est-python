print('-'*20)
print('LOJA SUPER BARATO')
print('-'*20)

mil = total = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        mil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if perg  == 'N':
        break
print('-' * 10, 'PROGRAMA ENCERRADO', '-' * 10)
print(f'O total da compra foi R${total:.2f}')
print(f'Produtos custando mais de R$1.000,00: {mil}')
print(f'O produto mais barato foi: {barato} custando R${menor:.2f}')