#########################################################################################################
# Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a  #
# pagar.                                                                                                #
#########################################################################################################
preço = float(input('Preço: '))
desconto = float(input('% do desconto: '))
d = preço * (desconto / 100)
pf = preço - d
print(f"""O desconto será de R${d:.2f}
Preço final: R${pf:.2f}""")