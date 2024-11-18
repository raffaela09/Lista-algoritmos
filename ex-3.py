temperatura_c = input('Digite uma temperatura em C: ')

temperatura_c_int = int(temperatura_c)

temperatura_f = temperatura_c_int * 1.8 + 32 

print(f'A temperatura {temperatura_c_int} em Fahrenheit é {temperatura_f:.2f}')