import re
palavra_1 = re.sub(r'[^a-zA-Z]','',input('Digite uma palavra: ')).lower()
palavra_2 = re.sub(r'[^a-zA-Z]','',input('Digite outra palavra que seja anagrama: ')).lower()


def e_anagrama():
    if len(palavra_1) != len(palavra_2):
        return False
    
    anagrama = {}
    anagrama_2 = {}
    for letra in palavra_1:
        if letra in anagrama:
            anagrama[letra] += 1
        else: 
            anagrama[letra] = 1
            
    for letra in palavra_2:
        if letra in anagrama_2:
            anagrama[letra] += 1
        else: 
            anagrama[letra] = 1
    return anagrama == anagrama_2
    
    
            
resultado = e_anagrama()
if resultado:
    print(f'As palavras {palavra_1} e {palavra_2} são anagramas.')
else:
    print(f'As palavras {palavra_1} e {palavra_2} não são anagramas.')
