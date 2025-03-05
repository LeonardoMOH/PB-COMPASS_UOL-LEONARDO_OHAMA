import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

from pyspark.sql.functions import col, row_number, explode, split, to_date, year, month, dayofmonth
from pyspark.sql.window import Window

## @params: [JOB_NAME, S3_INPUT_PATH, S3_INPUT_PATH_2, S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_INPUT_PATH_2', 'S3_TARGET_PATH'])

# Inicializacao do Job no Glue

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminho dos arquivos Parquet no S3

parquet_1 = args['S3_INPUT_PATH']
parquet_2 = args['S3_INPUT_PATH_2']

# Leitura dos arquivos Parquet no S3

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

# Cria as tabelas dimensao para ano, mes e dia

dim_ano = df_fato.select(year(col("data_lancamento")).alias("ano")).distinct()
dim_mes = df_fato.select(month(col("data_lancamento")).alias("mes")).distinct()
dim_dia = df_fato.select(dayofmonth(col("data_lancamento")).alias("dia")).distinct()

# Adiciona IDs unicos para cada dimensao

dim_ano = dim_ano.withColumn("id_ano", row_number().over(Window.orderBy("ano")))
dim_mes = dim_mes.withColumn("id_mes", row_number().over(Window.orderBy("mes")))
dim_dia = dim_dia.withColumn("id_dia", row_number().over(Window.orderBy("dia")))

# Adiciona os IDs de ano, mes e dia a tabela fato

df_fato = (
    df_fato
    .join(dim_ano, year(col("data_lancamento")) == col("ano"), "left")
    .join(dim_mes, month(col("data_lancamento")) == col("mes"), "left")
    .join(dim_dia, dayofmonth(col("data_lancamento")) == col("dia"), "left")
)

# Remove a coluna ano, mes e dia da tabela fato

df_fato = df_fato.drop("ano", "mes", "dia")

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

# Remove os valores nulos da tabela bridge_genero

bridge_genero = bridge_genero.dropna(subset=["id_bridge_genero"])

# Caminho de saida no S3

output_path = args['S3_TARGET_PATH']

# Converte para DynamicFrame e grava no Glue Catalog utilizando o args do target_path e todos no formato parquet

dim_titulo_dyf = DynamicFrame.fromDF(dim_titulo, glueContext, "dim_titulo")
dim_ano_dyf = DynamicFrame.fromDF(dim_ano, glueContext, "dim_tempo")
dim_mes_dyf = DynamicFrame.fromDF(dim_mes, glueContext, "dim_tempo")
dim_dia_dyf = DynamicFrame.fromDF(dim_dia, glueContext, "dim_tempo")
dim_genero_dyf = DynamicFrame.fromDF(dim_genero, glueContext, "dim_genero")
bridge_genero_dyf = DynamicFrame.fromDF(bridge_genero, glueContext, "bridge_genero")
df_fato_dyf = DynamicFrame.fromDF(df_fato, glueContext, "fato_filme")

glueContext.write_dynamic_frame.from_options(dim_titulo_dyf, connection_type="s3", connection_options={"path": output_path + "dimtitulo/dim_titulo/"}, format="parquet")
glueContext.write_dynamic_frame.from_options(dim_ano_dyf, connection_type="s3", connection_options={"path": output_path + "dimano/dim_ano/"}, format="parquet")
glueContext.write_dynamic_frame.from_options(dim_mes_dyf, connection_type="s3", connection_options={"path": output_path + "dimmes/dim_mes/"}, format="parquet")
glueContext.write_dynamic_frame.from_options(dim_dia_dyf, connection_type="s3", connection_options={"path": output_path + "dimdia/dim_dia/"}, format="parquet")
glueContext.write_dynamic_frame.from_options(dim_genero_dyf, connection_type="s3", connection_options={"path": output_path + "dimgenero/dim_genero/"}, format="parquet")
glueContext.write_dynamic_frame.from_options(bridge_genero_dyf, connection_type="s3", connection_options={"path": output_path + "bridgegenero/bridge_genero/"}, format="parquet")
glueContext.write_dynamic_frame.from_options(df_fato_dyf, connection_type="s3", connection_options={"path": output_path + "fatofilme/fato_filme/"}, format="parquet")

print("Exportacao concluida para o S3 e Glue Catalog!")

# Finaliza o job

job.commit()