import json
import os

# Caminho dos arquivos JSON
path = 'Sprint 7/Desafio/json'

# Nome dos filmes que foram escolhidos nas perguntas da Sprint 6
movies = ['Psycho', 'The Shining', 'The Exorcist', 'Scream']

# Laco que percorre todos os arquivos JSON da pasta
for arquivo in os.listdir(path):
    arquivo_path = os.path.join(path, arquivo)

    # Carrega o arquivo JSON
    with open(arquivo_path, 'r') as file:
            data = json.load(file)

     # Verifica se os filmes se encontram nos arquivos
    for movie in data:
        if movie['original_title'] in movies:
            print(f"Filme encontrado no arquivo {arquivo}: {movie['original_title']} de ID: {movie['id']}")
