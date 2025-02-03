#Exercício 085 - Listas com pares e ímpares
num = [[],[]]
valores = []
for c in range(1,8):
    valores = int(input(f'Digite 0 {c}º valor: '))
    if valores % 2 == 0:
        num[0].append(valores)
    else:
        num[1].append(valores)

print('-='*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')