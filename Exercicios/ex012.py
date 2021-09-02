#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

prod = float(input('Digite o valor do produto: RS$'))
desc = prod * 5 / 100

print('O valor do produto com desconto é: RS${:.2f}'.format(desc))