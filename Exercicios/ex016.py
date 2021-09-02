#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porçãi inteira.
import math

n = float(input('Digite um numero quebrado: '))
print('O numero {} tem a parte inteira {}'.format(n, math.trunc(n)))