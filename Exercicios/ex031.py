#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

viagem = float(input('Digite a distancia da viagem: '))

if viagem <= 200:
    passagem = 0.50 * viagem
    print('Sua viagem curta custou {} R$'.format(passagem))
else:
    passagem = 0.45 * viagem 
    print('Sua viagem longa custou {} R$'.format(passagem))
