#Exercício 029 - Radar eletrônico

v = float(input('Qual a velocidade do seu carro? '))
if v > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h\n'
          'Você deve pagar uma multa de: R${:.2f}\n'
          'Tenha um bom dia. Dirija com segurança!'.format((v-80)*7.0))

print('Tenha um bom dia. Dirija com segurança!')