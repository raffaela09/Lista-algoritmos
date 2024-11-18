while True:
    nota_1 = input('Digite a primeira nota: ')
    nota_2 = input('Digite a segunda nota: ')
    nota_3 = input('Digite a terceira nota: ')
    
    try:
        nota_1_float = float(nota_1)
        nota_2_float = float(nota_2)
        nota_3_float = float(nota_3)
    except ValueError:
         #except ValueError para permitir que o usuário digite uma letra sem quebrar o código.
        print('Por favor, digite somente números!')
    media = (nota_1_float + nota_2_float + nota_3_float) / 3    
    print(f'A sua média aritmética é {media}')
    sair = input('Deseja tentar outra vez? ').lower().startswith('n')
    if sair:
        break