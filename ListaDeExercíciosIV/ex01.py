#########################################################################################################
# Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as      #
# funções max e min.                                                                                    #
#########################################################################################################
from random import randint
lista = [ ]
menor = maior = 0
for c in range(10):
    sorteado = randint(1, 100)
    lista.append(sorteado)
    if maior == 0:
        maior = sorteado
    if menor == 0:
        menor = sorteado
    if sorteado > maior:
        maior = sorteado
    if sorteado < menor:
        menor = sorteado

print(lista)
print(maior)
print(menor)