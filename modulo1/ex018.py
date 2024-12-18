#Exercício 018 - Seno, cosseno e tangente
import math
ang = float(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(ang))
c = math.cos(math.radians(ang))
t = math.tan(math.radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang,s))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang,c))
print('O ângulo de {} tem a TANGENTE DE {:.2f}'.format(ang,t))

#from math import radians, sin, cos, tan - Desse modo podemos excluir as menções a math no código
