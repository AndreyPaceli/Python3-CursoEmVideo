#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados. 

valor = int (input('Informe um numero: '))
u = valor // 1 % 10
d = valor // 10 % 10
c = valor // 100 % 10
m = valor // 1000 % 10
print('Analisando o numero {}'.format(valor))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m)) 