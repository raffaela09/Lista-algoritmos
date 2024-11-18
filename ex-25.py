numeros_int = [-4, -3, -2, -1, 0, 1, 2, 3, 4]

def lista_pares(lista):
    lista_par = []
    for n in lista:
        if n % 2 == 0: 
            lista_par.append(n)  
    return lista_par
        
lista_par = lista_pares(numeros_int)    
print(f'A lista de números pares é: {lista_par}')  
