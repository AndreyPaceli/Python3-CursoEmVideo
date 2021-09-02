#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
#ordem: km hm dam m dm cm mm

medida = float(input('Uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000

print('A medida de {}m corresponde a {}cm e {}mm'.format(medida, cm, mm))