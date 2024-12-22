#Exercício 072 - Número por Extenso
cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'novo',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {cont[num]}')
    else:
        print('Inválido. Tente novamente.')

    e = input('Deseja continuar? [S/N]' ).strip().upper()
    if e != 'S':
        break
