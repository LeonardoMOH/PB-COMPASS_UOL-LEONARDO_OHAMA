import requests
import json
from datetime import date
import boto3

# Input para a inclusao da chave do usuario e a url base para fazer os endpoints necessarios

api_key = input("Digite sua chave de API para realizar a consulta: ")

base_url = "https://api.themoviedb.org/3"

# Limite de registros e tamanho

max_file_size = 10 * 1000 * 1000
max_records = 100

# Variaveis que serao utilizadas para controlar o numero de paginas, arquivos, tamanho etc

movies_details_json = []
size_json = 0
page = 1
index = 1
total_records = 0

# Variaveis de datas para utilizacao posterior no bucket

data = date.today()
dia = data.day
mes = data.month
ano = data.year

# Utilizando o client na biblioteca boto3

s3 = boto3.client('s3')

# Variaveis

# Nome do bucket

bucket_name = 'desafio-final-aws-leonardo-ohama'

# Nome dos arquivos no bucket

json_movies = f'RAW/TMDB/JSON/{ano}/{mes}/{dia}/'

# Loop para gerar os arquivos JSON pelo endpoint discover (esse endpoint foi utilizado para filtrar os dados que para esse caso foi utilizado apenas os filmes de lingua inglesa, uma votacao de pelo menos 300, uma media de votacao do publico de 5 e com o genero Terror) e o movie id para gerar os valores de orcamento e receita

while True:

    # Pega as informacoes pelo endpoint discover

    discover_url = (f"{base_url}/discover/movie?api_key={api_key}&include_adult=false&include_video=false&language=en-US&page={page}&sort_by=vote_average.desc&vote_average.gte=5&vote_count.gte=300&with_genres=27&with_original_language=en")
    data_response = requests.get(discover_url).json()

    total_pages = data_response.get("total_pages", 0)
    results = data_response.get("results", [])

    if not results:
        break

    # Loop para gerar os dados com as colunas requisitadas para a analise

    for movie in results:

        # movie_id = movie["id"] é necessario para buscar as informacoes de orcamento e receita que sao omitidos no endpoint discover

        movie_id = movie["id"]
        movie_url = f"{base_url}/movie/{movie_id}?api_key={api_key}"
        movie_details = requests.get(movie_url).json()

        credits_url = f"{base_url}/movie/{movie_id}/credits?api_key={api_key}"
        credits_response = requests.get(credits_url).json()
        director = next(
            (member["name"] for member in credits_response.get("crew", []) if member["job"] == "Director"),
            "Desconhecido"
        )

        # Colunas que serao geradas no formato JSON

        movie_data = {
            "id": movie_id,
            "imdb_id": movie_details.get("imdb_id"),
            "original_language": movie.get("original_language"),
            "original_title": movie.get("original_title"),
            "popularity": movie.get("popularity"),
            "release_date": movie.get("release_date"),
            "vote_average": movie.get("vote_average"),
            "vote_count": movie.get("vote_count"),
            "budget": movie_details.get("budget"),
            "revenue": movie_details.get("revenue"),
            "director": director,
        }

        # Adiciona os dados em um arquivo JSON

        movies_details_json.append(movie_data)
        size_json = len(json.dumps(movies_details_json, indent = 4).encode("utf-8"))
        total_records += 1       

        if len(movies_details_json) >= max_records or size_json >= max_file_size:

            file_name = f"{json_movies}movies_{index}.json"

            try:
                s3.put_object(
                Bucket = bucket_name,
                Key = file_name,
                Body = json.dumps(movies_details_json, indent = 4),
                ContentType = "application/json"
            )
                print(f"O arquivo {file_name} teve um upload com sucesso!")

            except Exception as e:

                print(f"Erro ao fazer upload do arquivo no S3: {file_name}")

            # "Reseta" as informacoes dos filmes para comecar o proximo arquivo JSON

            movies_details_json = []
            size_json = 0
            index += 1

    # Verifica se chegou ao final das paginas

    page += 1
    if page > total_pages:
        break

# Grava em arquivos JSON os 100 registros ou 10 MB

if movies_details_json:
    file_name = f"{json_movies}movies_{index}.json"
    try:
        s3.put_object(
            Bucket = bucket_name,
            Key = file_name,
            Body = json.dumps(movies_details_json, indent = 4),
            ContentType="application/json"
        )
        print(f"O arquivo {file_name} teve um upload com sucesso!")

    except Exception as e:

        print(f"Erro ao fazer upload do arquivo no S3: {file_name}")
