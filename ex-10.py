while True:
    base = input('Digite a base do triângulo: ')
    altura = input('Digite a altura do triângulo: ')

    try:
        base_float = float(base)
        altura_float = float(altura)
    except ValueError:
        #except ValueError para permitir que o usuário digite uma letra sem quebrar o código.
        print('Digite em numeros!')
        
    area = (base_float * altura_float) / 2
    
    print(f'A área desse triângulo é {area}')

    sair = input('Deseja tentar outra vez? ').lower().startswith('n')
    if sair:
        break