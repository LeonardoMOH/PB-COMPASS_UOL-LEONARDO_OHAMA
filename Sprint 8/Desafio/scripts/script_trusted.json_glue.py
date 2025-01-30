import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# from pyspark.sql.functions import col
from datetime import date

## @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Data atual

current_date = date.today()
year = current_date.year
month = current_date.month
day = current_date.day

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Leitura dos arquivos JSON

files_json = [f"{source_file}/movies_{i}.json" for i in range(1, 13)]
df = spark.read.option("multiline", "true").json(files_json)

# Normalizar os tipos das colunas

type_column = {
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

# Alterar o tipo de cada coluna conforme o mapeamento

for column, dtype in type_column.items():
    df = df.withColumn(column, df[column].cast(dtype))

# Caminho final do output

output_dir = f"{target_path}/{year}/{month}/{day}/movies.parquet"

# Escreve o arquivo final em parquet no caminho do output

df.coalesce(1).write.mode("overwrite").parquet(output_dir)

# Finalizar o job

job.commit()
