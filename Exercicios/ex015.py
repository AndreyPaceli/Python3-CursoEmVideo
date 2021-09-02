#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quis ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa 60 Reais por dia e 0,15 por Km rodade.

dias = int (input('Quantos dias você alugou o carro: '))
km = float (input('Quantos Km você andou com o carro: '))

Dias = dias * 60
Km = km * 0.15
total = Dias + Km
print ('Você andou {}km em {} dias, o total a ser pago é: R${}'.format(km, dias, total))