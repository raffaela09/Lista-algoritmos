frase = input('Digite uma frase: ')
contar_carac = {}

def cont_letra():
    for letra in frase:
        if letra in contar_carac:
            contar_carac[letra] += 1
        else: 
            contar_carac[letra] = 1
    return contar_carac
            
resultado = cont_letra()
print(resultado, type(resultado))
