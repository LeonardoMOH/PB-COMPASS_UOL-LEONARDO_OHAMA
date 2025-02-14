from pyspark.sql import SparkSession

# Criar sessão Spark
spark = SparkSession.builder.appName("ParquetToCSV").getOrCreate()

# Caminho do arquivo Parquet
parquet_path = "C:/GitHub/PB-COMPASS_UOL-LEONARDO_OHAMA/Sprint 9/Desafio/parquet/LOCAL/fato_filme.parquet/part-00000-d59d3c6e-36ed-473c-bf8d-916f56024c08-c000.snappy.parquet"

# Ler o Parquet
df = spark.read.parquet(parquet_path)

# Salvar como CSV
output_path = "C:/GitHub/PB-COMPASS_UOL-LEONARDO_OHAMA/Sprint 9/Desafio/csv_2"
df.write.mode("overwrite").option("header", "true").csv(output_path)

print("Conversão concluída!")
