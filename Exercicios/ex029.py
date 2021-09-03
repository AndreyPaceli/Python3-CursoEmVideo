# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Quantos Km/h você estava dirigindo ? '))
if velocidade >80:
    print('QUER VOAR ???')
    multa = (velocidade-80) * 7
    print('Mutado no valor de R${} REAIS!'.format(multa))
else:
    print('Otímo, dirija com segurança e BOM DIA! S2')