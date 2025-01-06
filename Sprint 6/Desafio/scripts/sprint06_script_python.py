import pandas as pd

import boto3

from datetime import date

# Essas linhas de comando foram para verificar o encoding predominante nos datasets

# import chardet

# with open('Sprint 6/Desafio/csv/movies.csv', 'rb') as file:
#     result = chardet.detect(file.read(5000))
#     print(result)

# with open('Sprint 6/Desafio/csv/series.csv', 'rb') as file:
#     result = chardet.detect(file.read(5000))
#     print(result)

# Abrindo os CSVs, o encoding do arquivo esta no UTF-8, é colocado os delimitadores das colunas e é determinado que a coluna 3 é string por causa de erro de leitura

with open(
    '/data/csv/movies.csv',
    "r",
    encoding='utf-8'
) as arquivo:
    df_movies = pd.read_csv(arquivo, delimiter = '|', dtype = {3: str}, low_memory = False)

with open(
    '/data/csv/series.csv', 
    "r",
    encoding='utf-8'
) as arquivo:
    df_series = pd.read_csv(arquivo, delimiter = '|', dtype = {3: str}, low_memory = False)

# Variaveis de datas para utilizacao posterior no bucket

data = date.today()
dia = data.day
mes = data.month
ano = data.year

# Utilizando o profile boto3

session = boto3.Session(profile_name="boto3")

s3 = session.client('s3')

# Variaveis

# Nome do bucket

bucket_name = 'desafio-final-aws-leonardo-ohama'

# Caminho dos arquivos que vai ser feito o upload

csv_original_path_movies = '/data/csv/movies.csv'

csv_original_path_series = '/data/csv/series.csv'

# Nome dos arquivos no bucket

csv_original_movies = f'RAW/Local/CSV/Movies/{ano}/{mes}/{dia}/movies.csv'

csv_original_series = f'RAW/Local/CSV/Series/{ano}/{mes}/{dia}/series.csv'

# Criacao do bucket, o upload do arquivo do desafio e o download do dataset

try:
    s3.create_bucket(
        Bucket = bucket_name
    )
    print(f'O Bucket {bucket_name} foi criado!')

    s3.upload_file(csv_original_path_movies,
                   bucket_name,
                   csv_original_movies)
    print(f'O arquivo {csv_original_movies} teve um upload com sucesso.')

    s3.upload_file(csv_original_path_series,
                   bucket_name,
                   csv_original_series)
    print(f'O arquivo {csv_original_series} teve um upload com sucesso.')

except Exception as e:
    print(f'Erro ao criar o bucket {bucket_name}!')
