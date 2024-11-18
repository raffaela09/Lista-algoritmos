def fibonacci (n):
    fn_form = [1, 1]
    
    while len(fn_form) < n:
        lista_num = fn_form [-1] + fn_form [-2]   
        fn_form.append(lista_num)
    
    return fn_form[:n]
n = int(input('Digite um numero: '))
fn_list = fibonacci(n)
print(f"Os {n} primeiros números da sequência de Fibonacci são: {fn_list}")