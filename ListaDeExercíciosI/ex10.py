#########################################################################################################
# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de  #
# cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de    #
# vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.          #
#########################################################################################################
cigarros_por_dia = int(input('Média de cigarros fumados por dia: '))
anos =int(input('Você fumou quantos anos? '))
total_cigarros = anos * 365 * cigarros_por_dia
dias_a_menos = (total_cigarros * 10) / (24 * 60)
print(f'Você perdeu {dias_a_menos:.21} de vida.')