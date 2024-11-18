lista_aninhada = [ [1, 2, 2, 3, 4, 4],
    [5, 6, 6, 7, 8, 8],
    [9, 9, 10, 11, 11, 10]]

def lista_duplicados(lista_aninhada):
    lista_resultado = []
    
    for sublista in lista_aninhada:
        sublista_1 = []
        for item in sublista:
            if item not in sublista_1:
                sublista_1.append(item)
        lista_resultado.append(sublista_1)   
         
    return lista_resultado

resultado = lista_duplicados(lista_aninhada)
print(resultado)