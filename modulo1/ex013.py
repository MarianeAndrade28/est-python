# Exercício 013 - Reajuste salarial
s = float(input('Digite seu salário: R$ '))
aumento = float(s + (s * 0.15))
print('Salário Atual: R${:.2f}\nSalário com Aumento de 15%: R$ {:.2f}'.format(s,aumento))

#Outro modo de escrever a porcentagem: (s + (s * 15/100))