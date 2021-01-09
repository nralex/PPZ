#########################################################################################################
# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do      #
# usuário, mostrando uma mensagem de erro e voltando a pedir as informações.                            #
#########################################################################################################
while True:
    usuário = str(input('Usuário: '))
    senha = str(input('Senha: '))
    if usuário != senha:
        print(f'Seja be vindo(a) {usuário}!')
        break
    else:
        print('\033[31mErro! usuário e senha não podem ser iguais!\033[m')