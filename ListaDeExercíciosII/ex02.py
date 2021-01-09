#########################################################################################################
# Determine se um ano é bissexto. Verifique no Google como fazer isso...                                #
#########################################################################################################
ano = int(input('Informe o ano que deseja analizar: '))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f'{ano} é um ano bissexto. ')
else:
    print(f'{ano} não é um ano bissexto. ')