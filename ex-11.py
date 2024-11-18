import re
frase = re.sub(r'[^\w\s]', '',input('Digite a sua frase: ')).lower().split()
cont_palavra = {}

for palavra in frase:
    if palavra in cont_palavra:
        cont_palavra[palavra] +=1
    else:
        cont_palavra[palavra] = 1
    
palavra_unica = []
for palavra, count in cont_palavra.items():
    if count == 1:
        palavra_unica.append(palavra)
contador_unic = len(palavra_unica)
if palavra_unica:
        print(f'as palavras únicas são: {palavra_unica}, sendo {contador_unic} palavras (a) únicas(a)')
else:
    print('Não há palavras únicas nessa frase.')

