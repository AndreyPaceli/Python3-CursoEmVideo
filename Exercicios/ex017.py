#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math

ca = float (input('Digite o valor do cateto adjascente: '))
co = float (input('Digite o valor do cateto oposto: '))

#hip = (co ** 2 + ca ** 2) ** (1/2)
hip = math.hypot(co, ca)
print('A hipotenusa vai medir{:.2f}'.format(hip))