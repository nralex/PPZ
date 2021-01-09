#########################################################################################################
# Faça um programa que peça um inteiro positivo e o mostre invertido. Ex.: 1234 gera 4321               #
#########################################################################################################
número = int(input('Digite um número: '))
n = str(número)
n = n[::-1]
n = int(n)
print(f'{número} ao contrário fica assim: {n}')