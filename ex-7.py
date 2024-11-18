while True:
    palavra = input('Digite uma palavra: ')
    
    print(f'A palavra {palavra} invertida é {palavra[::-1]}')
    
    sair = input('Deseja tentar outra vez?').lower().startswith('n')
    
    if sair:
        break