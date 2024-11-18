import re
frase = input('Digite um texto curto: ').lower()
freq_cont = {}
frase = re.sub(r'[^\w\s]', '', frase)
palavras_1 = frase.split()
for palavra in palavras_1:
    if palavra in freq_cont:
        freq_cont[palavra] +=1
    else:
        freq_cont[palavra] = 1
        
def palavras_freq(n=5):
    palavras_ordenadas = sorted(freq_cont.items(), key=lambda x: x[1], reverse=True)
    print('As palavras mais frequentes no texto são: ')
    for i in range(n):
        palavra, count = palavras_ordenadas[i]
        print(f'{i+1}. A palavra "{palavra}" apareceu {count} vezes')
palavras_freq()