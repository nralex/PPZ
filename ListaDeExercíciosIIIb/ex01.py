#############################################################################################################
# Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos.        #
# Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é triangular. #
#############################################################################################################
número = int(input('N: '))
n = 1
while n * (n + 1) * (n + 2) < número:
    n += 1
print(n * (n + 1) * (n + 2) < número)