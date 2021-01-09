#########################################################################################################
# Verifique se um inteiro positivo n é primo.                                                           #
#########################################################################################################
n = int(input('Digite um número: '))
para_comparar = [1, n]
divisível_por = []
for c in range(1, n + 1):
    if n % c == int():
        divisível_por.append(c)
if divisível_por == para_comparar or n == 1:
    print(f'{n} é um número primo.')
else:
    print(f'{n} não é um número primo.')