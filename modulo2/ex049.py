#Exercício 049 - Tabuada v.2.0
#Reformulando o Ex009, dessa vez com bem menos linhas

n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(n,c,n*c))
