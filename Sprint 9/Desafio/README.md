# Sumário

### Desafio:

1. [Script de Python para o Glue](scripts/GLUE/script_refined_glue_spark.py)

2. [Script de Python Local](scripts/LOCAL/script_refined_local_spark.py)

3. [Arquivo Parquet da tabela fato_filme](parquet/GLUE/part-00000-32f41a81-2c46-47c9-8a60-514577dccd56-c000.snappy.parquet)

4. [Arquivo Parquet da tabela dim_titulo](parquet/GLUE/part-00000-74d09563-078f-4d10-ac04-b4953011ffe5-c000.snappy.parquet)

5. [Arquivo Parquet da tabela dim_tempo](parquet/GLUE/part-00000-74d09563-078f-4d10-ac04-b4953011ffe5-c000.snappy.parquet)

6. [Arquivo Parquet da tabela dim_genero](parquet/GLUE/part-00000-74d09563-078f-4d10-ac04-b4953011ffe5-c000.snappy.parquet)

7. [Arquivo Parquet da tabela bridge_genero](parquet/GLUE/part-00000-74d09563-078f-4d10-ac04-b4953011ffe5-c000.snappy.parquet)

1. [Etapas](#etapas)

    I.    [Etapa 1 - Explicação camada Refined](#Etapa1)

    II.   [Etapa 2 - Script Python Local/Glue](#Etapa2)

    III.  [Etapa 3 - Script Python/Pyspark JSON](#Etapa3)

    IV.   [Etapa 4 - Criação do Crawler e AWS Athena](#Etapa4)
    
    V.  [Observações](#Observacoes)

2. [Anexos](#anexos)

    I.    [Anexo 1 - Versão VSCode](#Anexo1)

    II.   [Anexo 2 - Versão Pyspark](#Anexo2)

    III.  [Anexo 3 - Versão Java](#Anexo3)

    IV.   [Anexo 4 - Visualização do arquivo Parquet no VSCode (CSV)](#Anexo4)

    V.    [Anexo 5 - Visualização do arquivo Parquet no VSCode (JSON)](#Anexo5)

### README:

1. [README Principal](../../README.md)

2. [README Sprint 9](../README.md)

<a id="Etapas"></a>

# Etapas

Explicação do desenvolvimento da extração dos dados dos filmes pela API TMDB. Para o desenvolvimento foi utilizado o VSCode Version 1.96.4 (Release Date 16/01/2025), [winutils - hadoop 3.0 (GitHub de onde o arquivo foi baixado)](https://github.com/steveloughran/winutils/tree/master),Pyspark version 3.5.4, Java version "11.0.25" 2024-10-15  para mais informações: [Anexo 1 - Versão VSCode](#Anexo1), [Anexo 2 - Versão Pyspark](#Anexo2), [Anexo 3 - Versão Java](#Anexo3). 

<a id="Etapa1"></a>

1. ... [Etapa 1 - Explicação camada Refined](#Etapa1)

    Para processar os dados da camada Trusted para a Refined é necessário verificar novamente se não tem dados nulos e/ou duplicados. Depois utilizar somente os dados que serão utilizados, ou seja, colunas e valores que não vão ser utilizados na análise final não deverão estar no arquivo parquet da Refined e no final efetuar o processo de confecção das tabelas fato e dimensão.

    No processo de tratamento de dados, primeiro foi feito scripts executados localmente que foi feito o "debugging" do script e depois foi adaptado para ser utilizado no AWS Glue.
  
[**Voltar ao Sumário**](#sumário)

<a id="Etapa2"></a>

2. ... [Etapa 2 - Script Python Local/Glue](#Etapa2)

    No início começo do script é primeiro importado as bibliotecas que serão utilizadas no script local é importado a biblioteca que vai iniciar do Spark, as funções SQL utilizadas via Spark e o Window que vai auxiliar no tratamento das tabelas.

    Após isso, é iniciado a sessão do Spark e declarado a variável onde está localizado os arquivos parquets que serão processados, assim é utilizado a função função spark.read.option() para a leitura deles e é criado dois dataframes (df1 é o parquet do arquivo CSV e o df2 é correspondente ao parquet do arquivo JSON da API do TMDB) e depois disso é criado uma nova tabela que vai dar origem as tabelas fato e dimensão, com isso é utilizado as funções SQL join(), filter() que vai retirar as linhas que de budget e revenue iguais a 0 e por último a função select que vai selecionar cada coluna que vai ser utilizada para a análise final, vale ressaltar que também é colocado as colunas em português para uma melhor visualização dos dados.

    Agora é criado uma "janela" que vai particionar pela coluna titulo_original e depois é ordenado pelo id_filme. Na próxima linha é feito uma nova variável que correspondente a tabela dimensão título que vai ser criado uma coluna "row/linha" que será o número de linhas contidas pelo id_filme feita pela partição da "janela" e depois é retirado essa coluna "row". Esse procedimento foi feito para caso tenham linhas duplicadas e depois cria-se um id_titulo para cada linha com a função row_number().

    ![Evidência](../Evidencias/Desafio/ETAPA2_1_-_SCRIPT_LOCAL_CSV.png)

    Na linha seguinte vai ser feita o tratamento para a tabela dim_genero, só que no arquivo csv/parquet original os gêneros estão separados por vírgulas, assim primeiro é feito a "explosão" para guardar esses gêneros em linhas separadas que vão pertecer a tabela bridge_genero. Depois disso é feito a váriavel dim_genero e vai ser feito o mesmo procedimento anterior da criação dos IDs, que nesse caso é o id_genero que cada ID vai corresponder a um gênero.
    
    Na tabela bridge_genero será feita o join entre o df_genero que foi criado e o dim_genero que contém os IDs de cada gênero, nessa tabela vai conter 3 colunas, a coluna id_bridge_genero e o id_genero. No select vai ter somente o id_filme e o id_genero, porém o id_filme vai ser utilizado somente para auxiliar na construção do id_bridge_genero.
    
    ![Evidência](../Evidencias/Desafio/ETAPA2_2_-_SCRIPT_LOCAL_CSV.png)
    
    ![Evidência](../Evidencias/Desafio/ETAPA2_3_-_SCRIPT_LOCAL_CSV.png)

    <a id="Resultado_csv"></a>


    ![Evidência](../Evidencias/Desafio/ETAPA2_11_-_SCRIPT_GLUE_CSV.png)

    As configurações no Glue foram:

    - Glue 3.0
    - Worker Type G.1X
    - Max Capacity: 2 DPUs
    - Number of workers: 2
    - Timeout: 5 min
    - --S3_INPUT_PATH - s3://desafio-final-aws-leonardo-ohama/RAW/Local/CSV/Movies/2025/1/3/movies.csv
    - --S3_TARGET_PATH - s3://desafio-final-aws-leonardo-ohama/Trusted/Local/Parquet/movies/movies.parquet

    ![Evidência](../Evidencias/Desafio/ETAPA2_12_-_JOB_CSV_GLUE.png)

    ![Evidência](../Evidencias/Desafio/ETAPA2_13_-_CSV_INPUT_PATH.png)

    ![Evidência](../Evidencias/Desafio/ETAPA2_14_-_CSV_TARGET_PATH.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa3"></a>

3. ... [Etapa 3 - Script Python/Pyspark JSON](#Etapa3)

    ![Evidência](../Evidencias/Desafio/ETAPA3_9_-_JSON_TARGET_PATH.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa4"></a>

4. ... [Etapa 4 - Criação do Crawler e AWS Athena](#Etapa4)

    ![Evidência](../Evidencias/Desafio/ETAPA4_1_-_CRAWLER_CSV_GLUE.png)

[**Voltar ao Sumário**](#sumário)

<a id="Observacoes"></a>

6. ... [Observações](#Observacoes)

[**Voltar ao Sumário**](#sumário)

## Anexos

<a id="Anexo1"></a>

1. ... [Anexo 1 - Versão VSCode](#Anexo1)

    ![Evidência](../Evidencias/Desafio/ANEXO1_1_-_VERSAO_VSCODE.png)

[**Voltar para Etapas**](#Etapas)

[**Voltar ao Sumário**](#sumário)

<a id="Anexo2"></a>

2. ... [Anexo 2 - Anexo 2 - Versão Pyspark](#Anexo2)

    ![Evidência](../Evidencias/Desafio/ANEXO2_1_-_VERSAO_PYSPARK.png)

[**Voltar para Etapas**](#Etapas)

[**Voltar ao Sumário**](#sumário)

<a id="Anexo3"></a>

3. ... [Anexo 3 - Versão Java](#Anexo3)

    ![Evidência](../Evidencias/Desafio/ANEXO3_1_-_VERSAO_JAVA_PYSPARK.png)

[**Voltar para Etapas**](#Etapas)

[**Voltar ao Sumário**](#sumário)

<a id="Anexo4"></a>

3. ... [Anexo 4 - Visualização do arquivo Parquet no VSCode (CSV)](#Anexo3)

    ![Evidência](../Evidencias/Desafio/ANEXO4_1_-_VISUALIZACAO_PARQUET_CSV_VSCODE.png)

[**Voltar para Etapas**](#Etapas)

[**Voltar ao Sumário**](#sumário)

<a id="Anexo5"></a>

3. ... [Anexo 5 - Visualização do arquivo Parquet no VSCode (JSON)](#Anexo3)

    ![Evidência](../Evidencias/Desafio/ANEXO5_1_-_VISUALIZACAO_PARQUET_JSON_VSCODE.png)

[**Voltar para Etapas**](#Etapas)

[**Voltar ao Sumário**](#sumário)
