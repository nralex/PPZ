#########################################################################################################
# Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um terceiro    #
# vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois      #
# outros vetores. Imprima os três vetores.                                                              #
#########################################################################################################
from random import randint
v1 = []
v2 = []
v3 = []
for c in range(10):
    n1 = randint(1, 100)
    n2 = randint(1, 100)
    v1.append(n1)
    v2.append(n2)
    v3.append(n1)
    v3.append(n2)
print(v1)
print(v2)
print(v3)
