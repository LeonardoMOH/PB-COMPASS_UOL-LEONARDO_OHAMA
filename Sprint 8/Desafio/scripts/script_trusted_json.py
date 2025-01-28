from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import when, col

from datetime import date

spark = SparkSession \
        .builder \
        .master ("local[*]") \
        .appName("Desafio JSON") \
        .getOrCreate()

data = date.today()
dia = data.day
mes = data.month
ano = data.year

files_json = [f"Sprint 7/Desafio/json/movies_{i}.json" for i in range(1,13)]

df = spark.read.option("multiline", "true").json(files_json)

df.show(5)

# Encontrar linhas com valores nulos em qualquer coluna
nulls_colunm = df.filter(
    col("id").isNull() 
    | col("imdb_id").isNull() 
    | col("original_language").isNull()
    | col("original_title").isNull()
    | col("popularity").isNull()
    | col("release_date").isNull()
    | col("vote_average").isNull()
    | col("vote_count").isNull()
    | col("budget").isNull()
    | col("revenue").isNull()
    | col("director").isNull()
)
nulls_colunm.show()

# all_columns = df.columns

# df = df.na.fill("Desconhecido")

# for column in all_columns:
#     df = df.withColumn(column, when(col(column) == 0, "Desconhecido").otherwise(col(column)))

# df.show(5)

# Normalizar os tipos das colunas

type_colunm = {
    "id": "int",
    "imdb_id": "string",
    "original_language": "string",
    "original_title": "string",
    "popularity": "float",
    "release_date": "date",
    "vote_average": "float",
    "vote_count": "int",
    "budget": "int",
    "revenue": "int",
    "director": "string"
}

for column, dtype in type_colunm.items():
    df = df.withColumn(column, df[column].cast(dtype))

path = 'Sprint 8/Desafio/parquet/LOCAL/movies_tmdb.parquet'

df.coalesce(1).write.mode("overwrite").parquet(path)
