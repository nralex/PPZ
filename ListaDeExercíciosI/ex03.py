#########################################################################################################
# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.              #
# Calcule o total em segundos.                                                                          #
#########################################################################################################
d = int(input('Dias: '))
h = int(input('Horas: '))
m = int(input('Minutos: '))
s = int(input('Segundos: '))
total_segundos = (d * 24 * 60 *60) + (h * 60 * 60) + (m *60) + s
print(f'{d} dias, {h} horas, {m} minútos e {s} segundos têm {total_segundos} segundos. ')