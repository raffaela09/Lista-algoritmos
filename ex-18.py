def diagonal_soma_principal(matriz):
    soma = 0
    for i in range(3):
        soma += matriz[i][i]
    return soma

matriz = [[1,3,4],[3,5,9], [8,5,4]]
resultado = diagonal_soma_principal(matriz)
print(f'A soma da diagonal principal é {resultado}.')

def diagonal_soma_secundaria(matriz):
    soma_2 = 0
    for i in range(3):
        soma_2 += matriz[i][2-i]
    return soma_2
resultado_2 = diagonal_soma_secundaria(matriz)
print(f'A soma da diagonal secundária é {resultado_2}.')