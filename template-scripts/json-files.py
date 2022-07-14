import json

dict = {'nome': 'Guido Van Rossum',
        'linguagem': 'Python',
        'similar': ['c','modula3','lisp'],
        'users':1000000 }

# CONVERTE DICIONARIO EM OBJETO JSON

json_str = json.dumps(dict)

# CRIA ARQUIVO JSON

file = 'E:\\Google Drive\\Educação\\Python\\Algoritmos Exemplo\\json.json'
with open(file, 'w') as f:
    f.write(json_str)

## LEITURA ARQUIVO JSON

with open(file, 'r') as f:
    text = f.read()
    dict2 = json.loads(text)
    
## IMPRIMINDO JSON DA INTERNET

from urllib.request import urlopen
# Extrái html do link e converte em string
url = 'http://vimeo.com/api/v2/video/57733101.json'
response = urlopen(url).read().decode('utf8') 
# converte string do link para dicionario
dict3 = json.loads(response)[0]