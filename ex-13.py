notas = list(map(int, input('Digite as notas separadas por espaço: ').split()))
soma = sum(notas)
media = soma / len(notas)
lista_notas = [] 
for n in notas:  
    if n > media:
       lista_notas.append(n)
  
print('As notas maiores do que a média são: ', lista_notas)
        