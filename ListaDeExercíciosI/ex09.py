#########################################################################################################
# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,    #
# assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que #
# o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.                                               #
#########################################################################################################
dias = int(input('Dias: '))
km = int(input('Km rodados: '))
total = (dias * 60) + (km * 0.15)
print(f'Valor total a apagar R${total:.2f}')