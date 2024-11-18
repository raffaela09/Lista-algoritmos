while True:
    idade = input('Digite a sua idade (em numeros): ')
   
    try: 
     idade_int = int(idade)
    except ValueError:
        #except ValueError para permitir que o usuário digite uma letra sem quebrar o código.
        print('Digite somente números!')
        continue
    if idade_int > 18:
        print('Parabéns! Você já é de maior.')
    else:
        print('Você é de menor.')
    sair = input('Deseja sair? ').lower().startswith('s')
    if sair:
        break