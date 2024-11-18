from random import randint
print('Jogo da adivinhação, seja bem-vindo')
name = input('Qual o seu nome? ')
print(f'Olá {name}, tente adivinhar o numero que eu pensei, ele estará entre 1 e 100.')
number = randint(1,100)
num_try = 1
par = 5
while True:
    print(f'Tentativa {num_try}')
    while True:
        number_user = input('Que numero eu pensei? ')
        number2 = number_user.isdigit()
        if number2: 
            number_user_int = int(number_user)
            break
        else:
            print('Digite um numero inteiro.')
        
    acertou = number == number_user_int
    menor = number > number_user_int
    maior = number < number_user_int 
    if acertou:
        print(f'Parabens, voce acertou na tentativa {num_try}!!')
        break
    elif menor:
        if number - par <= number_user_int < number:
            print('Voce está perto!!')
        print(f'O numero {number_user_int} é menor doq eu pensei, tente novamente:')
        
    elif maior: 
        if number <  number_user_int < number + par:
            print('Voce está perto!!')
        print(f'O número {number_user_int} é maior doq eu pensei, tente novamente:')
    num_try +=1