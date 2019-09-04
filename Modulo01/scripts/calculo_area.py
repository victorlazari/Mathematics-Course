print('\n#### Script para cálculo de área de uma esfera.\n\n\n')

raio = input('#### Insira o raio do círculo a ser calculado.\n\n')

import math

print('\n\n#### Para calcular a área de um círculo a Fórmula utilizada é a:\n\n')
print('#### A = 4 * pi*r^2\n\n')

res = 4 * math.pi * math.pow(float(raio),2)

print('\n\n#### Resultado: ', res,'\n\n')