# calculadora com while
while True:
    prim_numero = input('Digite o primeiro numero: ')
    seg_numero = input('Digite o primeiro numero: ')
    operador = input('Digite o operador(+-/*): ')
    
    numeros_validos = None
    prim_numero_float = 0
    seg_numero_float = 0
    try:
        prim_numero_float = float(prim_numero)
        seg_numero_float = float(seg_numero)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Um ou ambos os numeros digitados não são válidos.')
        continue
    
    operadores_permitidos = '+-/*'
    
    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue
    if len(operador) > 1:
        print('Digite um único operador.')
        continue
    print('realizando sua conta, veja o resultado abaixo: ')
    if operador == '+':
        print(f'{prim_numero_float}+{seg_numero_float}=', prim_numero_float + seg_numero_float)
    elif operador == '-':
        print(f'{prim_numero_float}-{seg_numero_float}=', prim_numero_float - seg_numero_float)
    elif operador == '/':
        print(f'{prim_numero_float}/{seg_numero_float}=', prim_numero_float / seg_numero_float)
    elif operador == '*':
        print(f'{prim_numero_float}*{seg_numero_float}=', prim_numero_float * seg_numero_float)
    else:
        print('não deve chegar aq')
    
    sair = input('Deseja sair? [s]im: ').lower().startswith('s')
    
    if sair:
        break
    print(sair)