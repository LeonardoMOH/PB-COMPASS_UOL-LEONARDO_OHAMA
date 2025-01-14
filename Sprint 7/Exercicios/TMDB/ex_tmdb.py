import requests
import pandas as pd
from IPython.display import display
import json

api_key = input("Digite sua chave de API para realizar a consulta: ")

url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"

response = requests.get(url)
data = response.json()

while True:
   json_resp = input("Deseja criar um arquivo JSON? Digite S para sim e N para não: ").upper()
  
   if json_resp == "S":
      with open("Sprint 7/Exercicios/TMDB/JSON/filmes.json", "w", encoding = "UTF-8") as json_file:
        json.dump(data, json_file, ensure_ascii = False, indent = 4)
      break
   elif json_resp == "N":
      break
   else:
      print("Digite uma entrada válida!")

filmes = []

for movie in data['results']:
    df = {
        'Titulo': movie['title'],
        'Data de lançamento': movie['release_date'],
        'Visão geral': movie['overview'],
        'Votos': movie['vote_count'],
        'Média de votos:': movie['vote_average']
          }
    
filmes.append(df)

df = pd.DataFrame(filmes)
display(df)
