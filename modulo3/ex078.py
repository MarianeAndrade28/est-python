#Exercício 078 - Maior e menor valores na lista
valores = []
mai = 0
men = 0

for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < men:
            men = valores[c] 

print('='*30)
print(f'Você digitou os valores: {valores}')
print(f'O MAIOR valor digitado foi: {mai}, na(s) posição(s) ',end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O MENOR valor digitado foi: {men}, na(s) posição(s) ', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}...', end='')
print('\nFIM')