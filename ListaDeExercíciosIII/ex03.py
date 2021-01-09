#########################################################################################################
# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de          #
# crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.  #
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A    #
# ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento                          #
#########################################################################################################
a = 80_000
b = 200_000
contador = 1
while True:
    a *= 1.03
    b *= 1.015
    contador += 1
    if a >= b:
        print(f'São necessários {contador} anos para que a população do país A ultrapasse a população do país B')
        break
