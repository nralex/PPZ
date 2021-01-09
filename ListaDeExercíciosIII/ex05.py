#########################################################################################################
# Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o          #
# algoritmo de Euclides.                                                                                #
#########################################################################################################
a = 23_732
b = 180
while b != 0:
    r = a % b
    a = b
    b = r
print(a)