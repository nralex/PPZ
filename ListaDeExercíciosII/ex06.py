#########################################################################################################
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.      #
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o    #
# Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto,  #
# quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto -      #
# Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme a tabela abaixo:      #
#       a. + Salário Bruto : R$                                                                         #
#       b. - IR (11%) : R$                                                                              #
#       c. - INSS (8%) : R$                                                                             #
#       d. - Sindicato ( 5%) : R$                                                                       #
#       e. = Salário Liquido : R$                                                                       #
#########################################################################################################
valor_hora = float(input('Quanto você ganha por hora? R$ '))
número_de_horas = int(input('Número de horas trabalhadas no mês? '))
salário_bruto = valor_hora * número_de_horas
ir = salário_bruto * 0.11
inss = salário_bruto * 0.08
sindicato = salário_bruto * 0.05
salário_líquido = salário_bruto - ir - inss - sindicato
print(f"""+ {'Salário Bruto ':.<20}: R$ {salário_bruto:>8.2f}
- {'IR (11%) ':.<20}: R$ {ir:>8.2f}
- {'INSS (8%) ':.<20}: R$ {inss:>8.2f}
- {'Sindicato (5%) ':.<20}: R$ {sindicato:>8.2f}
= {'Salário Liquido ':.<20}: R$ {salário_líquido:>8.2f}
""")