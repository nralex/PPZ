#########################################################################################################
# Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu algoritmo deve ler o #
# valor da conta a ser paga e o valor do pagamento efetuado desprezando os centavos. Suponha que as     #
# notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que nenhuma delas esteja em falta no caixa.#
#########################################################################################################
compra = int(input('Valor da compra: R$'))
pagamento = int(input('Valor do pagamento: R$'))
troco = pagamento - compra
print(f'Troco: R$ {troco:.2f}')
c50 = c20 = c10 = c5 = c2 = c1 = 0
while True:
    if troco >= 50:
        troco -= 50
        c50 += 1
    elif troco >= 20:
        troco -= 20
        c20 += 1
    elif troco >= 10:
        troco -= 10
        c10 += 1
    elif troco >= 5:
        troco -= 5
        c5 += 1
    elif troco >= 2:
        troco -= 2
        c2 += 1
    elif troco >= 1:
        troco -= 1
        c1 += 1
    elif troco == 0:
        break
print(f"""
{c50} cédulas de R$ 50.00
{c20} cédulas de R$ 20.00
{c10} cédulas de R$ 10.00
{c5} cédulas de R$ 5.00
{c2} cédulas de R$ 2.00
{c1} cédulas de R$ 1.00
""")
