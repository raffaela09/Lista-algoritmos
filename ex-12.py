def primo(n):
    if n <=1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1,2):
        if n % i == 0:
            return False
    return True
def primos_range(comeco, fim):
    primos = []
    for num in range(comeco, fim+ 1):
        if primo(num):
            primos.append(num)
    return primos
comeco = int(input('Digite o inicio do seu intervalo:'))
fim = int(input('Digite o fim do seu intervalo: ')) 
primos = primos_range(comeco, fim)
print(f'Os numeros primos entre {comeco} e {fim} são {primos}')   