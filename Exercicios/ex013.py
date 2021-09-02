#Faça um algoritmo que leia o salálio de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite seu salário: R$'))
novoSal = salario + (salario * 15 / 100)

print('O novo salário do funcionario é: R${}'.format(novoSal))