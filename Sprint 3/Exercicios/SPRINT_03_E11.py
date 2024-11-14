import json

with open('person.json', 'r') as arquivo_json:
    conteudo_json = json.load(arquivo_json)

print(conteudo_json)