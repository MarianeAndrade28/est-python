#Exercício 034 - Aumentos múltiplos

s = float(input('Qual é o salário do funcionário? R$'))
if s <= 1250:
    a = s * 0.15 + s
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(s,a))
else:
    a = s * 0.10 + s
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(s,a))