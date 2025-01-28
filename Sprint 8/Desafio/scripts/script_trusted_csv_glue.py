import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

from pyspark.sql.functions import col, when
from pyspark.sql import functions as F

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

dynamic_frame = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_file]},
    format="csv",
    format_options={"withHeader": True, "separator": "|"}
)

df = dynamic_frame.toDF()

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

# Removendo valores duplicados

df = df.dropDuplicates()

# Normalizar os tipos das colunas

df = df.filter(
    col("genero").contains("Horror") | col("genero").contains("Mystery")
)

# Cria uma particao do parquet

df = df.repartition(1)

# Grava o arquivo no target_path

df.write.mode("overwrite").parquet(target_path)

# Finaliza o job

job.commit()
