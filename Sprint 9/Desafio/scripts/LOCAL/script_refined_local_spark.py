from pyspark.sql import SparkSession
from pyspark.sql.functions import col, row_number, explode, split, to_date, year, month, dayofmonth
from pyspark.sql.window import Window

# Cria a sessao do Spark

spark = SparkSession.builder.appName("ETL_Filmes").getOrCreate()

# Caminho dos arquivos Parquet

parquet_1 = "C:/GitHub/PB-COMPASS_UOL-LEONARDO_OHAMA/Sprint 8/Desafio/parquet/GLUE/part-00000-32f41a81-2c46-47c9-8a60-514577dccd56-c000.snappy.parquet"
parquet_2 = "C:/GitHub/PB-COMPASS_UOL-LEONARDO_OHAMA/Sprint 8/Desafio/parquet/GLUE/part-00000-74d09563-078f-4d10-ac04-b4953011ffe5-c000.snappy.parquet"

# Realiza a leitura dos dois arquivos parquet (CSV e JSON)

df1 = spark.read.parquet(parquet_1)
df2 = spark.read.parquet(parquet_2)

# Nova tabela que servira de base para a construcao da tabela fato e dimensao

df_filme = (
    df1.alias("t1")
    .join(df2.alias("t2"), col("t1.id") == col("t2.imdb_id"))
    .filter((col("t2.budget") != 0) & (col("t2.revenue") != 0))
    .select(
        col("t1.id").alias("id_filme"),
        col("t1.tempoMinutos").alias("tempo_minutos"),
        col("t1.genero"),
        col("t2.original_title").alias("titulo_original"),
        col("t2.popularity").alias("popularidade"),
        col("t2.release_date").alias("data_lancamento"),
        col("t2.budget").alias("orcamento"),
        col("t2.revenue").alias("receita"),
        col("t2.vote_average").alias("media_votos"),
        col("t2.vote_count").alias("total_votos"),
    )
)

# Cria a tabela dimensao titulo mantendo apenas um id_filme por titulo

window_spec_titulo = Window.partitionBy("titulo_original").orderBy("id_filme")
dim_titulo = df_filme.withColumn("row", row_number().over(window_spec_titulo))
dim_titulo = dim_titulo.filter(col("row") == 1).drop("row")

# Cria um ID para cada titulo (com base no id_filme correto)

window_spec_id_titulo = Window.orderBy("id_filme")
dim_titulo = dim_titulo.withColumn("id_titulo", row_number().over(window_spec_id_titulo))

# "Explosao" da coluna genero para criar uma tabela auxiliar que retira as virgulas se tiver mais de um genero

df_genero = df_filme.select("id_filme", explode(split(col("genero"), ",")).alias("genero"))

# Cria uma lista unica de generos com IDs consistentes

dim_genero = df_genero.select("genero").distinct()
window_spec_genre = Window.orderBy("genero")
dim_genero = dim_genero.withColumn("id_genero", row_number().over(window_spec_genre))

# Cria uma tabela de associacao filme-genero (bridge)

bridge_genero = (
    df_genero.alias("gen")
    .join(dim_genero.alias("dgen"), col("gen.genero") == col("dgen.genero"))
    .select(
        col("gen.id_filme"),
        col("dgen.id_genero")
    )
    .distinct()
)

# Cria a tabela fato

df_fato = (
    df_filme.alias("f")
    .join(dim_titulo.alias("tit"), "id_filme")
    .select(
        col("f.id_filme"),
        col("tit.id_titulo"),
        col("f.data_lancamento"),
        col("f.tempo_minutos"),
        col("f.popularidade"),
        col("f.orcamento"),
        col("f.receita"),
        col("f.media_votos"),
        col("f.total_votos"),
    )
    .distinct()
)

# Cria uma tabela dimensao (dim_tempo) apenas com as datas presentes na tabela fato

dim_tempo = df_fato.select("data_lancamento").distinct()
window_spec = Window.orderBy("data_lancamento")
dim_tempo = dim_tempo.withColumn("id_tempo", row_number().over(window_spec))

# Faz a extracao do ano, mes e dia da coluna data_lancamento

dim_tempo = dim_tempo.withColumn("ano", year(col("data_lancamento")))
dim_tempo = dim_tempo.withColumn("mes", month(col("data_lancamento")))
dim_tempo = dim_tempo.withColumn("dia", dayofmonth(col("data_lancamento")))

# Converte a coluna data_lancamento para o formato de data

dim_tempo = dim_tempo.withColumn("data_lancamento", to_date(col("data_lancamento")))

# Adiciona o id_tempo a tabela fato

df_fato = df_fato.join(dim_tempo, on="data_lancamento", how="inner")

# Remove a coluna data_lancamento, ano, mes e dia da tabela fato

df_fato = df_fato.drop("data_lancamento", "ano", "mes", "dia")

# Adiciona o id_bridge_genero a tabela fato

window_spec_fato = Window.orderBy("id_filme")
df_fato = df_fato.withColumn("id_bridge_genero", row_number().over(window_spec_fato))

# Adiciona o id_bridge_genero a tabela bridge_genero

bridge_genero = bridge_genero.join(df_fato.select("id_filme", "id_bridge_genero"), on="id_filme", how="left")

# Seleciona apenas as colunas necessarias na tabela bridge_genero

bridge_genero = bridge_genero.select("id_bridge_genero", "id_genero")

# Remove o id_filme da tabela dim_titulos e seleciona apenas as colunas dessa tabela

dim_titulo = df_fato.join(
    dim_titulo.alias("dim_tit"),
    df_fato.id_filme == col("dim_tit.id_filme"),
    "left"
).select(
    col("dim_tit.id_titulo"),
    col("dim_tit.titulo_original")
)

# # Remove o id_filme da dim_titulos

# dim_titulo = dim_titulo.select("id_titulo", "titulo_original")

# Remove os valores nulos da tabela bridge_genero

bridge_genero = bridge_genero.dropna(subset=["id_bridge_genero"])

# Exporta todas as tabelas dimensão e fato em formato Parquet

output_path = "C:/GitHub/PB-COMPASS_UOL-LEONARDO_OHAMA/Sprint 9/Desafio/parquet/LOCAL/"

dim_titulo.write.mode("overwrite").parquet(output_path + "dim_titulo.parquet")
dim_tempo.write.mode("overwrite").parquet(output_path + "dim_tempo.parquet")
dim_genero.write.mode("overwrite").parquet(output_path + "dim_genero.parquet")
bridge_genero.write.mode("overwrite").parquet(output_path + "bridge_genero.parquet")
df_fato.write.mode("overwrite").parquet(output_path + "fato_filme.parquet")

print("Exportação concluída!")