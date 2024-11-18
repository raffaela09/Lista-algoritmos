lista = [-5, 3, -1, 0, 2, 3, 4, -1, 7, 2, 9, 4, 15, 3]


def remover_duplicados(lista):
    lista_sem_duplicados = []
    for n in lista:
        if n not in lista_sem_duplicados:
          lista_sem_duplicados.append(n)
    return lista_sem_duplicados

resultado = remover_duplicados(lista)
print(resultado)  
    
