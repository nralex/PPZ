#########################################################################################################
# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da    #
# área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e    #
# que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades    #
# de latas de tinta a serem compradas e o preço total.                                                  #
# Obs. : somente são vendidos um número inteiro de latas.                                               #
#########################################################################################################
metros = float(input('Informe a área ser pintada: [m²] '))
cobertura = 3
volume_da_lata = 18
preço_da_lata = 80
número_de_latas = metros / (cobertura * volume_da_lata)
if número_de_latas == int(número_de_latas):
    número_de_latas = int(número_de_latas)
else:
    número_de_latas = int(número_de_latas) + 1
print(f'Para pintar {metros} m² será necessária a compra de:\n{número_de_latas} lata(s) de tinta.\nAo custo de R${número_de_latas * preço_da_lata:.2f}')