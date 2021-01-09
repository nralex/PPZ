#########################################################################################################
# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido  #
# e continue pedindo até que o usuário informe um valor válido.                                         #
#########################################################################################################
while True:
    try:
        nota = int(input('Informe uma nota entre 0 e 10 '))
    except:
        nota = 11
        print('\033[31mErro! Informe uma opção válida!\033[m')
    if 1 <= nota <= 10:
        print('Obrigado!')
        break
    else:
        print('\033[31mErro! Informe uma opção válida!\033[m')