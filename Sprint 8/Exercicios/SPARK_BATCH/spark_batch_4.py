from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext

spark = SparkSession \
        .builder \
        .master ("local[*]") \
        .appName("Exercicio Intro") \
        .getOrCreate()

path = 'Sprint 8/Exercicios/SPARK_BATCH/txt/nomes_aleatorios.txt'

df_nomes = spark.read.csv(path)

df_nomes.show(5)

# Imprimir o schema do dataframe
df_nomes.printSchema()

# Renomear a coluna do dataframe para nome
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

df_nomes.show(10)
df_nomes.printSchema()

# Importa bibliotecas random e when, o random para gerar aleatoriedade da condicao e o when que é a condicional

from pyspark.sql.functions import rand, when

# Adicionar a coluna Escolaridade com valores aleatórios entre Fundamental (60%), Médio(30%) e Superior(10%)

df_nomes = df_nomes.withColumn(
    "Escolaridade",
    when(rand() < 0.60, "Fundamental")
    .when(rand() < 0.90, "Médio")
    .otherwise("Superior"))

df_nomes.show(10)
df_nomes.printSchema()

# Cria a coluna Pais e coloca paises da America do Sul com probabilidade 1/13

df_nomes = df_nomes.withColumn(
    "Pais",
    when(rand() < 1/13, "Argentina")
    .when(rand() < 2/13, "Bolivia")
    .when(rand() < 3/13, "Brasil")
    .when(rand() < 4/13, "Chile")
    .when(rand() < 5/13, "Colombia")
    .when(rand() < 6/13, "Equador")
    .when(rand() < 7/13, "Guiana")
    .when(rand() < 8/13, "Paraguai")
    .when(rand() < 9/13, "Peru")
    .when(rand() < 10/13, "Suriname")
    .when(rand() < 11/13, "Uruguai")
    .when(rand() < 12/13, "Venezuela")
    .otherwise("Guiana Francesa")
)

df_nomes.show(10)
df_nomes.printSchema()

# Importa a biblioteca floor que é para arredondamento

from pyspark.sql.functions import floor

# Cria uma nova coluna AnoNascimento que os valores vao variar entre 1945 a 2010

df_nomes = df_nomes.withColumn("AnoNascimento", floor(rand() * 65 + 1945).cast("int"))

df_nomes.show(10)
df_nomes.printSchema()

# Importa a biblioteca col que ajuda a manipulacao das colunas

from pyspark.sql.functions import col

# Cria um novo dataframe e filtra os valores do AnoNascimento para maior ou igual a 2000

df_select = df_nomes.select("Nomes",
                            "Escolaridade",
                            "Pais",
                            col("AnoNascimento").cast("int").alias("AnoNascimento")) \
                    .filter(col("AnoNascimento") >= 2000)

df_select.show(10)

# Cria uma view chamada pessoas

df_nomes.createOrReplaceTempView ("pessoas")

# Utiliza a funcao spark.sql que vai utilizar as funcoes do SQL que nesse caso é o mesmo da Etapa 6

spark.sql("""
    SELECT
        Nomes,
        Escolaridade,
        Pais,
        AnoNascimento
    FROM pessoas
    WHERE AnoNascimento >= 2000
""").show()

# Um novo dataframe que vai contar o numero de pessoas entre 1980 a 1994

df_millennials = df_nomes.select("Nomes",
                            "Escolaridade",
                            "Pais",
                            col("AnoNascimento").cast("int").alias("AnoNascimento")) \
                    .filter(col("AnoNascimento").between(1980, 1994))

linhas = df_millennials.count()
print(linhas)

# Cria uma nova view chamada pessoas_2

df_nomes.createOrReplaceTempView ("pessoas_2")

# Conta a quantidade de pessoas de 1980 a 1994 que deve ser a mesma que a etapa 8

df_millennials = spark.sql("""
    SELECT COUNT(*) AS Total
    FROM pessoas
    WHERE AnoNascimento >= 1980
    AND AnoNascimento <= 1994
""")

df_millennials.show()

# Cria uma view pessoas_3

df_nomes.createOrReplaceTempView("pessoas_3")

# Cria um novo dataframe utilizando a funcao spark.sql que vai criar uma nova coluna chamada Geracao que vai distribuir em valores diferentes de geracoes

df_final = spark.sql("""
    SELECT
        CASE
            WHEN AnoNascimento >= 1944 AND AnoNascimento <= 1964 THEN 'Baby Boomers'
            WHEN AnoNascimento >= 1965 AND AnoNascimento <= 1979 THEN 'Geracao X'
            WHEN AnoNascimento >= 1980 AND AnoNascimento <= 1994 THEN 'Millennials (Geracao Y)'
            WHEN AnoNascimento >= 1995 AND AnoNascimento <= 2015 THEN 'Geracao Z'
        END AS Geracao,
        Pais,
        COUNT(*) AS Quantidade
    FROM pessoas_3
    GROUP BY
        CASE
            WHEN AnoNascimento >= 1944 AND AnoNascimento <= 1964 THEN 'Baby Boomers'
            WHEN AnoNascimento >= 1965 AND AnoNascimento <= 1979 THEN 'Geracao X'
            WHEN AnoNascimento >= 1980 AND AnoNascimento <= 1994 THEN 'Millennials (Geracao Y)'
            WHEN AnoNascimento >= 1995 AND AnoNascimento <= 2015 THEN 'Geracao Z'
        END,
        Pais
    ORDER BY Pais, Geracao, Quantidade DESC
""")

df_final.show()
