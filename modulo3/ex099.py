#Exercício 099 - Função que descobre o maior
from time import sleep

def linha():
    print('-=' *30,)
    
def maior(* num):
    cont = maior = 0
    print('Analisando parâmetros...')
    sleep(0.5)

    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

#Programa Principal
maior(2,9,4,5,7,1)
linha()
maior(4,7,0)
linha()
maior(1,2)
linha()
maior(6)
linha()
maior()
linha()