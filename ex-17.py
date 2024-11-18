lista = [-7, 4, -3, 12, -15, 9, 0, 2, -8, 5, -1, 6, -11, 3]
lista_negativo = []
lista_positivo = []
def lista_org():
    for n in lista:
        if n < 0:
            lista_negativo.append(n)
        elif n >= 0:
            lista_positivo.append(n)
    lista_negativo.extend(lista_positivo)
    return lista_negativo
resultado = lista_org()
print(resultado)      
