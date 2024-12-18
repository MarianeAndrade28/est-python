#Exercício 051 - Progressão Aritmética

print('='*25)
print('10 TERMOS DE UMA PA')
print('='*25)

t1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = t1 + (10 - 1) * razao

for cont in range(t1,decimo + razao,razao):
    print(cont, end=' -> ')

print('FIM!')