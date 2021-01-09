#########################################################################################################
# Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32                          #
#########################################################################################################
temperatura = int(input('Temperatura [°C] '))
f = (9 * temperatura) / 5 + 32
print(f'{temperatura}° = {f:.1f}F')