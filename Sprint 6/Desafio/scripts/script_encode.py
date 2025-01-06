import chardet

import pandas as pd

with open('Sprint 6/Desafio/csv/movies.csv', 'rb') as file:
    result = chardet.detect(file.read(5000))
    print(result)

with open('Sprint 6/Desafio/csv/series.csv', 'rb') as file:
    result = chardet.detect(file.read(5000))
    print(result)

# with open(
#     'Sprint 6/Desafio/csv/movies.csv',
#     "r",
#     encoding='utf-8'
# ) as arquivo:
#     df_movies = pd.read_csv(arquivo, delimiter = '|')

# with open(
#     'Sprint 6/Desafio/csv/series.csv', 
#     "r",
#     encoding='utf-8'
# ) as arquivo:
#     df_series = pd.read_csv(arquivo, delimiter = '|')

with open(
    'Sprint 6/Desafio/csv/movies.csv',
    "r",
    encoding='utf-8'
) as arquivo:
    df_movies = pd.read_csv(arquivo, delimiter = '|', dtype = {3: str}, low_memory = False)

with open(
    'Sprint 6/Desafio/csv/series.csv', 
    "r",
    encoding='utf-8'
) as arquivo:
    df_series = pd.read_csv(arquivo, delimiter = '|', dtype = {3: str}, low_memory = False)
