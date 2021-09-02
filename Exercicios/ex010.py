#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere US$1,00 = R$3,27

valor = float(input('Digite o valor da sua carteira: R$'))
dolar = valor / 3.27

print('Considerando seu dinheiro RS${:.2f}, você poderia comprar US${:.2f}'.format(valor, dolar))