#########################################################################################################
# A sequência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...                          #
# Sua regra de formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento  #
# é a soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número de    #
# Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.                                                               #
#########################################################################################################
n = int(input('Quantos números deseja ver na sequencia de Fibonacci? '))
n1 = n2 = 1
print(n1, end=' ')
for c in range(1, n):
    print(n2, end=' ')
    n1, n2 = n2, n1 + n2 # Atribuição múltipla
