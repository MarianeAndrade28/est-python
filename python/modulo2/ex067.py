#Exercício 067 - Tabuada v3.0
while True:
    t = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if t < 0:
        break
    for c in range(1,11):
        print(f'{t} x {c} = {t*c}')
    print('-' * 30)
print('Programa Encerrado!')