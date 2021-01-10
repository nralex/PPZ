#########################################################################################################
# Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu algoritmo deve ler o #
# valor da conta a ser paga e o valor do pagamento efetuado desprezando os centavos. Suponha que as     #
# notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que nenhuma delas esteja em falta no caixa.#
#########################################################################################################
compra = int(input('Valor da compra: R$'))
pagamento = int(input('Valor do pagamento: R$'))
troco = pagamento - compra
notas = [50, 20, 10, 5, 2, 1]
for nota in notas:
    while troco >= nota:
        print(f'Uma nota de {nota}')
        troco -= nota