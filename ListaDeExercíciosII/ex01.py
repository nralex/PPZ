#########################################################################################################
# Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores     #
# podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero,         #
# isósceles ou escaleno.                                                                                #
#########################################################################################################
a = int(input('Informe o comprimento do 1° segmento: '))
b = int(input('Informe o comprimento do 2° segmento: '))
c = int(input('Informe o comprimento do 3° segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('É um triângulo ', end='')
    if a == b == c:
        print('equilátero.')
    elif a == b or b == c or a == c:
        print('isósceles')
    else:
        print('escaleno')
else:
    print('Não é um triângulo')