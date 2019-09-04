print('\n#### Script para cálculo de volume de uma esfera.\n\n\n')

raio = input('#### Insira o raio do círculo a ser calculado.\n\n')

import math

print('\n\n#### Para calcular o volume de um círculo a Fórmula utilizada é a:\n\n')
print('#### V= 4/3*pi*r^3\n\n')

res = 4 * math.pi * math.pow(float(raio),2)

print('\n\n#### Resultado: ', res,'\n\n')