import re

vogais = ('a', 'e', 'i', 'o','u') 
   
def quant_letras(frase):
    vogais_quant = 0
    cons_quant = 0
    for letra in frase:
        if letra in vogais:
            vogais_quant += 1
        else: 
            cons_quant += 1
    return vogais_quant, cons_quant
           
entrada = re.sub(r'[^a-zA-Z]','',input('Digite uma frase: ')).lower()
vogais_quant, cons_quant = quant_letras(entrada)
print(f'O número de vogais é {vogais_quant} e o número de consoantes é {cons_quant}.')

