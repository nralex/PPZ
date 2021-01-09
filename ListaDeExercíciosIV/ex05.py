'''
“The Python Software Foundation and the global Python community welcome and encourage participation by everyone. 
Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other 
live up to these principles. We want our community to be more diverse: whoever you are, and whatever your 
background, we welcome you.”. 

Seja o mesmo texto acima “splitado”. 
Calcule quantas palavras possuem uma das letras “python” e que tenham mais de 4 caracteres. 
Não se esqueça de transformar maiúsculas para minúsculas e de remover antes os caracteres especiais.
'''

texto = """The Python Software Foundation and the global Python community welcome and encourage participation 
by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help 
each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever 
your background, we welcome you.
""".lower()
from string import punctuation
for c in punctuation:
    texto = texto.replace(c, ' ')


def buscaLetra(palavra):
    for letra in palavra:
        if letra in 'python':
            return True
    return False


python = []
for c in texto.split():
    if buscaLetra(c) and len(c) > 4:
        python.append(c)

print(python)
print(len(python))