#########################################################################################################
# Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média         #
# esperada para a viagem.                                                                               #
#########################################################################################################
distância = int(input('Distância: '))
velocidade = int(input('Velocidade: '))
tempo = distância / velocidade
print(f'Tempo de viagem {tempo:.1f} hora(s)')