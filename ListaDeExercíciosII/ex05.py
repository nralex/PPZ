#########################################################################################################
# Faça um Programa que leia três números e mostre o maior e o menor deles.                              #
#########################################################################################################
números = list()
for c in range(3):
    números.append(int(input(f'Informe o {c + 1}° número: ')))
print(f'O maior número informado foi: {min(números)}')