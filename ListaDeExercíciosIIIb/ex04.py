#########################################################################################################
# Dado um número inteiro positivo, determine a sua decomposição em fatores primos calculando também a   #
# multiplicidade de cada fator.                                                                         #
#########################################################################################################
número = int(input('Número: '))
for c in range(2, número):
    while número % c == 0:
        print(c)
        número = número / c