from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import when, col
from pyspark.sql import functions as F

spark = SparkSession \
        .builder \
        .master ("local[*]") \
        .appName("Desafio csv") \
        .getOrCreate()

file_csv = 'Sprint 8/Desafio/csv/movies.csv'

df = spark.read.option("delimiter", "|").csv(file_csv, header=True, inferSchema=True)

df.show(5)

# Encontrar linhas com valores nulos em qualquer coluna

nulls_colunm = df.filter(
    col("id").isNull() 
    | col("tituloPincipal").isNull() 
    | col("tituloOriginal").isNull()
    | col("anoLancamento").isNull()
    | col("tempoMinutos").isNull()
    | col("genero").isNull()
    | col("notaMedia").isNull()
    | col("numeroVotos").isNull()
    | col("generoArtista").isNull()
    | col("personagem").isNull()
    | col("nomeArtista").isNull()
    | col("anoNascimento").isNull()
    | col("anoFalecimento").isNull()
    | col("profissao").isNull()
    | col("titulosMaisConhecidos").isNull()
)
nulls_colunm.show()

# Quantidade de valores nulos por coluna

for colunm in df.columns:
    null_count = df.filter(F.col(colunm).isNull()).count()
    print(f"A coluna {colunm} tem {null_count} valores nulos.")

# Apenas a coluna profissao tem valores nulos, portanto os valores nulos serao substituidos por "Desconhecido"

df = df.na.fill({"profissao": "Desconhecido"})

# Encontrar linhas com valores nulos em qualquer coluna novamente

nulls_colunm = df.filter(
    col("id").isNull() 
    | col("tituloPincipal").isNull() 
    | col("tituloOriginal").isNull()
    | col("anoLancamento").isNull()
    | col("tempoMinutos").isNull()
    | col("genero").isNull()
    | col("notaMedia").isNull()
    | col("numeroVotos").isNull()
    | col("generoArtista").isNull()
    | col("personagem").isNull()
    | col("nomeArtista").isNull()
    | col("anoNascimento").isNull()
    | col("anoFalecimento").isNull()
    | col("profissao").isNull()
    | col("titulosMaisConhecidos").isNull()
)
nulls_colunm.show()

for colunm in df.columns:
    null_count = df.filter(F.col(colunm).isNull()).count()
    print(f"A coluna {colunm} tem {null_count} valores nulos.")

# Removendo valores duplicados

df = df.dropDuplicates()

# Renomear coluna tituloPincipal

df = df.withColumnRenamed("tituloPincipal", "tituloPrincipal")

# Normalizar os tipos das colunas

type_column = {
    "id": "string",
    "tituloPrincipal": "string",
    "tituloOriginal": "string",
    "anoLancamento": "int",
    "tempoMinutos": "int",
    "genero": "string",
    "notaMedia": "float",
    "numeroVotos": "int",
    "generoArtista": "string",
    "personagem": "string",
    "nomeArtista": "string",
    "anoNascimento": "int",
    "anoFalecimento": "int",
    "profissao": "string",
    "titulosMaisConhecidos": "string"
}

# Converter as colunas

for column, dtype in type_column.items():
    df = df.withColumn(column, df[column].cast(dtype))

df = df.filter(
    col("genero").contains("Horror") | col("genero").contains("Mystery"))

# rows = df.count()

# print(f"Número de linhas: {rows}")

# Output do parquet

path = 'Sprint 8/Desafio/parquet/LOCAL/movies_csv.parquet'

df = df.repartition(1)

df.write.mode("overwrite").parquet(path)
