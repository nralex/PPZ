'''
Daniela é uma pessoa muito supersticiosa. 
Para ela, um número é sortudo se ele contém o dígito 2 mas não o dígito 7. 
Então, na opinião dela, quantos números sortudos existem entre 18644 e 33087, incluindo os extremos?
Resposta: 7995
'''
contador = 0
for c in range(18_644, 33_088):
    if '2' in str(c) and '7' not in str(c):
        contador += 1
print(contador)