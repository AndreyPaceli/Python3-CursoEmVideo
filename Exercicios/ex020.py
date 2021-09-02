#Um programa para sortear a ordem de nomes, presentes em uma lista.

import random

n1 = str (input('Digite o nome do 1° aluno: '))
n2 = str (input('Digite o nome do 2° aluno: '))
n3 = str (input('Digite o nome do 3° aluno: '))
n4 = str (input('Digite o nome do 4° aluno: '))

lista = [n1,n2,n3,n4]
random.shuffle(lista)

print('A ordem será: ')
print(lista)