#########################################################################################################
# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a       #
# porcentagem do aumento. Exiba o valor do aumento e do novo salário.                                   #
#########################################################################################################
s = float(input('Salário: '))
p = float(input('% do aumento: '))
aumento = s * (p / 100)
salário = s + aumento
print(f"""O aumento será de R${aumento:.2f}
Assim o novo salário será R${salário:.2f}""")