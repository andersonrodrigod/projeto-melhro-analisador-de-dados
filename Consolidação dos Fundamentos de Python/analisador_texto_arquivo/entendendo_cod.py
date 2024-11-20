# Importação dos módulos necessários
from collections import Counter  # Counter é uma ferramenta que ajuda a contar ocorrências de elementos em uma lista
import re  # Expressões regulares para manipulação de texto

# Definindo o nome do arquivo a ser lido
arquivo = 'texto.txt'

# Abrindo o arquivo para leitura (modo "r") com codificação UTF-8
texto = open(arquivo, "r", encoding="utf-8")

# Lendo o conteúdo do arquivo inteiro e armazenando em uma variável
conteudo = texto.read()

# Usando uma expressão regular para encontrar todas as palavras no texto, convertendo tudo para minúsculo
conteudo_minusculo = re.findall(r'\b\w+\b', conteudo.lower())  # \b = palavra, \w+ = sequência de caracteres alfanuméricos

# Dividindo o texto em frases com base nos sinais de pontuação (. ! ?)
frases = re.split(r'[.!?]', conteudo)  # Divide onde houver ponto, exclamação ou interrogação

# Criando uma lista para armazenar frases que não sejam vazias
frases_filtradas = []
# Percorrendo todas as frases divididas
for frase in frases:
    frase = frase.strip()  # Removendo espaços extras no começo e fim da frase
    if frase:  # Verifica se a frase não está vazia
        frases_filtradas.append(frase)  # Adiciona a frase à lista se não estiver vazia

# Calculando o número total de caracteres no conteúdo do arquivo
num_caracteres = len(conteudo)

# Dividindo o conteúdo em palavras (usando espaços como delimitadores)
palavras = conteudo.split()

# Contando o número de palavras no texto
num_palavras = len(palavras)

# Contando o número de frases filtradas
num_frases = len(frases_filtradas)

# Definindo um conjunto de "stopwords", ou seja, palavras comuns que não devem ser contadas
stopwords = {"-----------------------------", "A", "já", "6", "foi", "as", "dos", "como", "os", "O", "era", "Eu", "meu", "à", "5", "O", "na", "em", "minha", "eu", "2", "mas", "mais", "do", "por", "no", "me", "não", "se", "da", "eu", "a", "o", "um", "para", "que", "é", "uma", "de", "com", "você", "e", "muito", "pode"}

# Criando uma lista para armazenar as palavras filtradas (sem as stopwords)
palavras_filtradas = []

# Percorrendo cada palavra e adicionando à lista se não estiver nas stopwords
for palavra in palavras:
    if palavra not in stopwords:  # Verifica se a palavra não está na lista de stopwords
        palavras_filtradas.append(palavra)  # Adiciona a palavra à lista de filtradas

# Contando a frequência das palavras filtradas usando o Counter
contagem = Counter(palavras_filtradas)

# Obtendo as 5 palavras mais comuns e suas frequências
mais_frequentes = contagem.most_common(5)

# Exibindo as 5 palavras mais frequentes e suas contagens
for palavra, frequencia in mais_frequentes:
    print(f"as palavras que mais aparecem são as seguintess:'{palavra}': {frequencia}")

# Exibindo o número de caracteres no texto
print(f'Número de caracteres: {num_caracteres}')

# Exibindo o número de palavras no texto
print(f'Número de palavras: {num_palavras}')

# Exibindo o número de frases no texto
print(f'Número de frases: {num_frases}')
