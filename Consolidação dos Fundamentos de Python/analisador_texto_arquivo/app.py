from collections import Counter
import re

arquivo = 'texto.txt'

with open(arquivo, "r", encoding="utf-8") as texto:
    conteudo = texto.read()

para_frase = conteudo

conteudo = re.sub(r'[^\w\s]', '', conteudo.lower())

frases = re.split(r'[.!?]\s*', para_frase)


frases_filtradas = []
for frase in frases:
    frase = frase.strip()
    if frase:
        frases_filtradas.append(frase)

# frases_filtradas = [frase.strip() for frase in frases if frase.strip()]

num_caracteres = len(conteudo)
palavras = conteudo.split()
num_palavras = len(palavras)
num_frases = len(frases_filtradas)

stopwords = {"-----------------------------", "A", "já", "6", "foi", "as", "dos","como", "os", "O", "era","Eu", "meu", "à", "5", "O", "na", "em", "minha", "eu", "2","mas", "mais", "do", "por", "no","me", "não", "se", "da", "eu", "a","o","um", "para", "que","é", "uma", "de", "com", "você", "e", "muito", "pode"}

palavras_filtradas = []

for palavra in palavras:
    if palavra not in stopwords:
        palavras_filtradas.append(palavra)

# palavras_filtradas = [palavra for palavra in palavras if palavra not in stopwords]

contagem = Counter(palavras_filtradas)
mais_frequentes = contagem.most_common(5)

for palavra, frequencia in mais_frequentes:
    print(f"as palavras que mais aparecem são as seguintess:'{palavra}': {frequencia}")

print(f'Número de caracteres: {num_caracteres}')
print(f'Número de caracteres de palavras: {num_palavras}')
print(f'Número de frases: {num_frases}')