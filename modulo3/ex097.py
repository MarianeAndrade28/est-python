#Exercício 097 - Um print especial
def escreva(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)

escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')