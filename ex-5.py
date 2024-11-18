while True:
    tabuada = 1
    number = input('Digite um numero: ')
    try:
        number_int = int(number)
    except ValueError:
        #except ValueError para permitir que o usuário digite uma letra sem quebrar o código.
        print('Por favor, digite um número inteiro') 
        continue 
    for tabuada in 10:
        tabuada_2 = tabuada * number_int           
        print(f'{tabuada} X {number_int} = {tabuada_2}')
        tabuada+=1

    if tabuada > 10:            
        sair = input('Deseja tentar outra vez?').lower().startswith('n')
        if sair:
            break