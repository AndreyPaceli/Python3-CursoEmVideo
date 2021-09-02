#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

a = input('Digite algo')
print('O tipo primitivo desse valor é ', type(a))
print('É alfabetico ? ', a.isalpha)
print('É alfabetico ? ', a.isalnum)
print('É alfabetico ? ', a.isupper)
print('É alfabetico ? ', a.islower)
print('É alfabetico ? ', a.istitle)
