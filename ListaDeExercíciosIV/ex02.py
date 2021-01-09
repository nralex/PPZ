#########################################################################################################
# Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os números     #
# ímpares na lista IMPAR. Imprima as três listas.                                                       #
#########################################################################################################
from random import randint
par = [ ]
impar = []
menor = maior = 0
for c in range(20):
    sorteado = randint(1, 100)
    if sorteado % 2 == 0:
        par.append(sorteado)
    else:
        impar.append(sorteado)

print(par)
print(impar)