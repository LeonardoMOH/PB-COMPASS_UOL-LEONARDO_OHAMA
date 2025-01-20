import requests
import json
from datetime import date
import boto3
import os

def lambda_handler(event, context):

    # Para a api_key do TMDB foi utilizado variavel de ambiente

    api_key = os.environ['API_KEY']

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

    # Nome do bucket

    bucket_name = 'desafio-final-aws-leonardo-ohama'

    # Nome dos arquivos no bucket

    json_movies = f'RAW/TMDB/JSON/{ano}/{mes}/{dia}/'

    # Loop para gerar os arquivos JSON pelo endpoint discover e o movie id para gerar os valores de orcamento e receita

    while True:

        # Pega as informacoes pelo endpoint discover

        discover_url = (f"{base_url}/discover/movie?api_key={api_key}&include_adult=false&include_video=false&language=en-US&page={page}&sort_by=vote_average.desc&vote_average.gte=5&vote_count.gte=300&with_genres=27&with_original_language=en")
        data_response = requests.get(discover_url).json()

        total_pages = data_response.get("total_pages", 0)
        results = data_response.get("results", [])

        # Caso nao tenha mais resultados o programa ira sair do loop

        if not results:
            break

        # Loop para gerar os dados com as colunas requisitadas para a analise

        for movie in results:

            # movie_id = movie["id"] é necessario para buscar as informacoes de orcamento e receita que sao omitidos no endpoint discover

            movie_id = movie["id"]
            movie_url = f"{base_url}/movie/{movie_id}?api_key={api_key}"
            movie_details = requests.get(movie_url).json()

            # Procedimento para pegar o diretor e para isso é necessario "pegar as informações" da producao do filme 

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
                "original_language": movie_details.get("original_language"),
                "original_title": movie_details.get("original_title"),
                "popularity": movie_details.get("popularity"),
                "release_date": movie_details.get("release_date"),
                "vote_average": movie_details.get("vote_average"),
                "vote_count": movie_details.get("vote_count"),
                "budget": movie_details.get("budget"),
                "revenue": movie_details.get("revenue"),
                "director": director,
            }

            # Adiciona os dados em um arquivo JSON

            movies_details_json.append(movie_data)
            size_json = len(json.dumps(movies_details_json, indent = 4).encode("utf-8"))
            total_records += 1       

            # Verifica se o arquivo JSON atingiu mais de 100 registros ou 10 MB

            if len(movies_details_json) >= max_records or size_json >= max_file_size:

                # Nome do arquivo

                file_name = f"{json_movies}movies_{index}.json"

                # Upload no Bucket

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

                # "Reseta" os detalhes dos filmes no arquivo JSON e adiciona o indice para mais um

                movies_details_json = []
                size_json = 0
                index += 1

        # Verifica se chegou ao final das paginas

        page += 1
        if page > total_pages:
            break

    # Grava o último arquivo JSON

    if movies_details_json:
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

    print(f"Total de filmes processados: {total_records}")
