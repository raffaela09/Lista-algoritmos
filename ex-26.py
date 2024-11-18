dicionario_1 = {'a': 6, 'b': 3, 'c': 7, 'e': 'rafa'}
dicionario_2 = {'a': 8, 'b': 8, 'd': 4, 'e': 'rafa_1'}


def dicionarios_juntos(dicionario_1, dicionario_2):
    
    resultado = dicionario_1.copy()
    
    for chave, valor in dicionario_2.items():
        if chave in resultado:
            resultado[chave]+= valor
        else:
            resultado[chave] = valor
            
    return resultado
            
            
resultado = dicionarios_juntos(dicionario_1, dicionario_2)
print(resultado)