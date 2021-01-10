#########################################################################################################
# Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o          #
# algoritmo de Euclides.                                                                                #
#########################################################################################################
a = 23_732
b = 180
while a % b != 0:
    a, b = b, a % b # Atribuição múltipla
print(b)