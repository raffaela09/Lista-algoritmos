while True:

    palavra = input('Digite uma palavra: ').lower()

    print(f'{palavra} = {palavra[::-1]}')
    if palavra[::-1] == palavra:
        print(f'Portanto, a palavra {palavra} é um palíndromo.')
    else:
        print(f'Portanto, a palavra {palavra} não é um palíndromo.') 
    
    sair = input('Deseja tentar outra vez? ').lower().startswith('n')
    
    if sair:
        break