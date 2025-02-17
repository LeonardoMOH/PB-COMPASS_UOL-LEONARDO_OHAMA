# Sumário

### Desafio:

1. [Script de Python para o Glue](scripts/GLUE/script_refined_glue_spark.py)

2. [Script de Python Local](scripts/LOCAL/script_refined_local_spark.py)

3. [Script SQL para o diagrama ER](sql/sql_er.sql)

4. [Script SQL que fez a verificação local dos arquivos gerados pelo Glue](sql/sql_verificacao.sql)

5. [Diagrama ER](../Evidencias/Desafio/ETAPA1_2_-_DIAGRAMA_ER.png)

6. [Arquivo Parquet da tabela fato_filme](parquet/GLUE/fato_filme/part-00000-fc2f153c-e568-420c-bebd-76fcf2de66f2-c000.snappy.parquet)

7. [Arquivo Parquet da tabela dim_titulo 1](parquet/GLUE/dim_titulo/part-00000-b1abff8d-51bf-458e-ab80-f1b52da55838-c000.snappy.parquet)

   [Arquivo Parquet da tabela dim_titulo 2](parquet/GLUE/dim_titulo/part-00001-b1abff8d-51bf-458e-ab80-f1b52da55838-c000.snappy.parquet)

   [Arquivo Parquet da tabela dim_titulo 3](parquet/GLUE/dim_titulo/part-00002-b1abff8d-51bf-458e-ab80-f1b52da55838-c000.snappy.parquet)

   [Arquivo Parquet da tabela dim_titulo 4](parquet/GLUE/dim_titulo/part-00003-b1abff8d-51bf-458e-ab80-f1b52da55838-c000.snappy.parquet)

8. [Arquivo Parquet da tabela dim_tempo](parquet/GLUE/dim_tempo/part-00000-7ab7338d-c230-4c5b-bf18-4b39a9c69c7e-c000.snappy.parquet)

9. [Arquivo Parquet da tabela dim_genero](parquet/GLUE/dim_genero/part-00000-2133655b-896c-4800-9335-2112edf81dea-c000.snappy.parquet)

10. [Arquivo Parquet da tabela bridge_genero 1](parquet/GLUE/bridge_genero/part-00000-cfe9595e-5f98-4d70-9022-5044169f52e8-c000.snappy.parquet)

   [Arquivo Parquet da tabela bridge_genero 2](parquet/GLUE/bridge_genero/part-00001-cfe9595e-5f98-4d70-9022-5044169f52e8-c000.snappy.parquet)

   [Arquivo Parquet da tabela bridge_genero 3](parquet/GLUE/bridge_genero/part-00002-cfe9595e-5f98-4d70-9022-5044169f52e8-c000.snappy.parquet)

   [Arquivo Parquet da tabela bridge_genero 4](parquet/GLUE/bridge_genero/part-00003-cfe9595e-5f98-4d70-9022-5044169f52e8-c000.snappy.parquet)

1. [Etapas](#etapas)

    I.    [Etapa 1 - Explicação camada Refined, construção do diagrama ER e perguntas que deverão ser respondidas na análise](#Etapa1)

    II.   [Etapa 2 - Script Python Local](#Etapa2)

    III.  [Etapa 3 - Script Python AWS Glue](#Etapa3)

    IV.   [Etapa 4 - Criação do Crawler e AWS Athena](#Etapa4)

    V.    [Etapa 5 - Verificação Local dos arquivos parquet gerados](#Etapa5)
    
    VI.   [Observações](#Observacoes)

2. [Anexos](#anexos)

    I.    [Anexo 1 - Versão VSCode](#Anexo1)

    II.   [Anexo 2 - Versão Pyspark](#Anexo2)

    III.  [Anexo 3 - Versão Java](#Anexo3)

    IV.   [Anexo 4 - Versão Dbeaver](#Anexo4)

    V.    [Anexo 5 - Alguns arquivos gerados na fase de debugging](#Anexo5)

### README:

1. [README Principal](../../README.md)

2. [README Sprint 9](../README.md)

<a id="Etapas"></a>

# Etapas

Explicação do desenvolvimento da ETL pelo Glue, na qual foi refinado os dados para a camada Refined. Para o desenvolvimento foi utilizado o VSCode Version 1.97.2 (Release Date 12/02/2025), [winutils - hadoop 3.0 (GitHub de onde o arquivo foi baixado)](https://github.com/steveloughran/winutils/tree/master),Pyspark version 3.5.4, Java version "11.0.25" 2024-10-15 e DBeaver Version 24.3.4.202502021521 Release Date 03/02/2025, para mais informações: [Anexo 1 - Versão VSCode](#Anexo1), [Anexo 2 - Versão Pyspark](#Anexo2), [Anexo 3 - Versão Java](#Anexo3), [Anexo 4 - Versão Dbeaver](#Anexo4).

<a id="Etapa1"></a>

1. ... [Etapa 1 - Explicação camada Refined, construção do diagrama ER e perguntas que deverão ser respondidas na análise](#Etapa1)

    Para processar os dados da camada Trusted para a Refined é necessário verificar novamente se não tem dados nulos e/ou duplicados. Depois utilizar somente os dados que serão utilizados, ou seja, colunas e valores que não vão ser utilizados na análise final não deverão estar no arquivo parquet da Refined e no final efetuar o processo de confecção das tabelas fato e dimensão.

    No processo de tratamento de dados, primeiro foi feito scripts executados localmente que foi feito o "debugging" do script e depois foi adaptado para ser utilizado no AWS Glue.

    Para a construção do diagrama ER foi feito um [script](sql/sql_er.sql) no DBeaver na tabela fato_filme ela irá agrupar todos os valores de ID(id_filme, id_titulo, id_tempo, id_bridge_genero) e também as principais colunas que serão analisadas como orçamento, receita, media_votos e popularidade.

    - Na tabela dim_titulo: id_titulo e o titulo_original;
    - Na tabela dim_tempo: id_tempo, data_lancamento, ano, mes e dia;
    - Na tabela dim_genero: id_genero, genero;
    - Na tabela bridge_genero: id_bridge_genero e id_genero.

    ![Evidência](../Evidencias/Desafio/ETAPA1_1_-_SCRIPT_SQL.png)

    ![Evidência](../Evidencias/Desafio/ETAPA1_2_-_DIAGRAMA_ER.png)

    As perguntas da Sprint 6 foram reformuladas para as seguintes perguntas:

    **Do Cinema ao Streaming: Como as Bilheterias e Tendências do Terror Foram Moldadas pelas Décadas e Revolucionadas pela Tecnologia**

    1) As bilheterias totais dos filmes mais populares do gênero terror de cada década. Elas têm aumentado a cada década? Qual foi a melhor década para os filmes populares de terror em termos de rentabilidade para o gênero terror?

    2) Comparar os filmes listados (que são uns dos mais populares), a seguir que começam da década de 60 até os dias atuais om os filmes do mesmo gênero em sua respectiva década.

    - Psycho (Psicose) - 1960-1970;
    - The Exorcist (O Exorcista) - 1970-1980;
    - The Shining (O Iluminado) - 1980-1990;
    - The Blair Witch Project (A Bruxa de Blair) - 1990-2000;
    - Saw (Jogos Mortais) - 2000-2010;
    - Get Out (Corra) - 2010-2020;
    - The Invisible Man (O Homem Invisível) - 2020-2024.

        Esses filmes foram os mais rentáveis de seu ano em seus respectivos gêneros em relação a média dos outros filmes dessa década?

    3) Os filmes lançados perto do Halloween (31 de outubro) tiveram uma maior bilheteria em relação aos outros filmes? E em relação aos filmes populares listados anteriormente? Se algum desses filmes foi lançado próximo a essa data, como seu desempenho se compara aos demais?

    4) Agora compare entre os filmes da questão 2. Os filmes de maior orçamento tiveram maior bilheteria? Os filmes pré-década de 90 ainda são populares nos dias de hoje?

    5) Há alguma relação entre a duração do filme e sua popularidade ou a bilheteria? E os filmes que têm o gênero além do terror, qual foi o desempenho delas em suas bilheterias?

    6) Com o surgimento da internet na década de 70 e a popularização de redes sociais na internet nos anos 2000, houve impacto na bilheteria?

    7) O impacto da popularização do streaming afetou a bilheteria? Considere que streamings como Netflix começaram a ficar popular em 2016, ou seja, comparar os dados de bilheterias de antes dessa data com as de depois dessa data.
    
[**Voltar ao Sumário**](#sumário)

<a id="Etapa2"></a>

2. ... [Etapa 2 - Script Python Local](#Etapa2)

    Primeiro será mostrado o script local, no início dele é primeiro importado as bibliotecas que serão utilizadas no script local é importado a biblioteca que vai iniciar do Spark, as funções SQL utilizadas via Spark e o Window que vai auxiliar no tratamento das tabelas.

    Após isso, é iniciado a sessão do Spark e declarado a variável onde está localizado os arquivos parquets que serão processados, assim é utilizado a função função spark.read.option() para a leitura deles e é criado dois dataframes (df1 é o parquet do arquivo CSV e o df2 é correspondente ao parquet do arquivo JSON da API do TMDB) e depois disso é criado uma nova tabela que vai dar origem as tabelas fato e dimensão, com isso é utilizado as funções SQL join(), filter() que vai retirar as linhas que de budget e revenue iguais a 0 e por último a função select que vai selecionar cada coluna que vai ser utilizada para a análise final, vale ressaltar que também é colocado as colunas em português para uma melhor visualização dos dados.

    Agora é criado uma "janela" que vai particionar pela coluna titulo_original e depois é ordenado pelo id_filme. Na próxima linha é feito uma nova variável que correspondente a tabela dimensão título que vai ser criado uma coluna "row/linha" que será o número de linhas contidas pelo id_filme feita pela partição da "janela" e depois é retirado essa coluna "row". Esse procedimento foi feito para caso tenham linhas duplicadas e depois cria-se um id_titulo para cada linha com a função row_number().

    ![Evidência](../Evidencias/Desafio/ETAPA2_1_-_SCRIPT_LOCAL.png)

    Na linha seguinte vai ser feita o tratamento para a tabela dim_genero, só que no arquivo csv/parquet original os gêneros estão separados por vírgulas, assim primeiro é feito a "explosão" para guardar esses gêneros em linhas separadas que vão pertecer a tabela bridge_genero. Depois disso é feito a váriavel dim_genero e vai ser feito o mesmo procedimento anterior da criação dos IDs, que nesse caso é o id_genero que cada ID vai corresponder a um gênero.
    
    Na tabela bridge_genero será feita o join entre o df_genero que foi criado e o dim_genero que contém os IDs de cada gênero, nessa tabela vai conter 3 colunas, a coluna id_bridge_genero e o id_genero. No select vai ter somente o id_filme e o id_genero, porém o id_filme vai ser utilizado somente para auxiliar na construção do id_bridge_genero.
    
    Agora é criado o dataframe que será a tabela fato_filme na qual vai conter quase todos os IDs (id_filme, id_titulo, id_tempo, id_bridge_genero), porém nessas linhas não vão conter por enquanto todas esses IDs, vão ser adicionados após a tabela dimensão for feita correspondente a cada ID e também vai ter as colunas tempo_minutos, popularidade, orçamento, receita, media_votos e total_votos.
    
    Depois da criação da tabela fato, é criado a tabela a tabela dim_tempo para isso essa tabela vai ser baseada na coluna data_lancamento, com ela é criado o id_tempo com o mesmo procedimento feito na criação dos IDs anteriores.

    ![Evidência](../Evidencias/Desafio/ETAPA2_2_-_SCRIPT_LOCAL.png)
    
    E também será separado o ano, mês e dia da coluna para que seja facilmente consumido na hora da análise, no final da criação da tabela dim_tempo é feito a conversão da coluna para date.

    Diante disso, é adicionado o id_tempo na tabela fato e é removido as colunas da data_lancamento, ano, mes e dia e também é adicionado a coluna do id_bridge_genero que servirá de base para criar a tabela bridge_genero, com isso é feito o left join da tabela fato com a bridge_genero a partir do id_filme (id do imdb) e para finalizar a tabela bridge_genero é só colocado as duas colunas id_bridge_genero e id_genero via select.

    Na tabela dim_titulo é novamente feito um tratamento que irá confirmar a integridade dos dados que serão colocados nesta tabela com o auxílio do join. Assim é feito das colunas que serão somente utilizadas nessa tabela (id_titulo e titulo_original).

    ![Evidência](../Evidencias/Desafio/ETAPA2_3_-_SCRIPT_LOCAL.png)

    E no final é feito um tratamento final da tabela bridge_genero que como feito a join com os arquivos parquet do csv e JSON haviam valores que poderiam dar nulo.

    Chegando no final do script é feito a exportação de todos os arquivos parquet que são separados por cada tabela (dimensão e fato).

    ![Evidência](../Evidencias/Desafio/ETAPA2_4_-_SCRIPT_LOCAL.png)


[**Voltar ao Sumário**](#sumário)

<a id="Etapa3"></a>

3. ... [Etapa 3 - Script Python AWS Glue](#Etapa3)

    No script do Glue a maior diferença vai estar na importação das bibliotecas que vão ser feitas para o funcionamento do Glue e o caminho de input e output 

    ![Evidência](../Evidencias/Desafio/ETAPA3_1_-_SCRIPT_GLUE.png)

    ![Evidência](../Evidencias/Desafio/ETAPA3_2_-_SCRIPT_GLUE.png)

    ![Evidência](../Evidencias/Desafio/ETAPA3_3_-_SCRIPT_GLUE.png)

    ![Evidência](../Evidencias/Desafio/ETAPA3_4_-_SCRIPT_GLUE.png)

    ![Evidência](../Evidencias/Desafio/ETAPA3_5_-_SCRIPT_GLUE.png)

    ![Evidência](../Evidencias/Desafio/ETAPA3_6_-_SCRIPT_GLUE.png)

    ![Evidência](../Evidencias/Desafio/ETAPA3_7_-_SCRIPT_GLUE.png)

    ![Evidência](../Evidencias/Desafio/ETAPA3_8_-_SCRIPT_GLUE.png)

    ![Evidência](../Evidencias/Desafio/ETAPA3_9_-_SCRIPT_GLUE.png)

    As configurações no Glue foram:

    - Glue 3.0
    - Worker Type G.1X
    - Max Capacity: 2 DPUs
    - Number of workers: 2
    - Timeout: 10 min
    - --S3_INPUT_PATH - s3://desafio-final-aws-leonardo-ohama/Trusted/Local/Parquet/movies/movies.parquet/part-00000-32f41a81-2c46-47c9-8a60-514577dccd56-c000.snappy.parquet
    - --S3_INPUT_PATH_2 - s3://desafio-final-aws-leonardo-ohama/Trusted/TMDB/Parquet/movies/2025/1/20/movies.parquet/part-00000-ca2b239d-1800-4ea6-a5e8-aba00aecc374-c000.snappy.parquet
    - --S3_TARGET_PATH - s3://desafio-final-aws-leonardo-ohama/Refined/

    ![Evidência](../Evidencias/Desafio/ETAPA3_10_-_CONFIG_GLUE.png)

    ![Evidência](../Evidencias/Desafio/ETAPA3_11_-_CONFIG_GLUE.png)

    ![Evidência](../Evidencias/Desafio/ETAPA3_12_-_INPUT_PATH.png)

    ![Evidência](../Evidencias/Desafio/ETAPA3_13_-_INPUT_PATH_2.png)

    ![Evidência](../Evidencias/Desafio/ETAPA3_14_-_TARGET_PATH.png)

    Com isso pode-se ver que o Job do Glue rodou com sucesso.

    ![Evidência](../Evidencias/Desafio/ETAPA3_15_-_GLUE_JOB.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa4"></a>

4. ... [Etapa 4 - Criação do Crawler e AWS Athena](#Etapa4)

    Para o Crawler foi utilizado o nome movies_refined com as seguintes configurações:

    ![Evidência](../Evidencias/Desafio/ETAPA4_1_-_CONFIG_CRAWLER.png)

    Depois de criado o crawler é possível verificar que o crawler foi criado com sucesso.

    ![Evidência](../Evidencias/Desafio/ETAPA4_2_-_RUN_CRAWLER.png)

    E depois na aba tables pode-se ver que foram geradas as tabelas: fatofilme, dimtitulo, dimtempo, dimgenero, bridgegenero.

    ![Evidência](../Evidencias/Desafio/ETAPA4_3_-_TABELAS_CRAWLER.png)

    Com o Athena foram consultadas as tabelas fazendo select das primeiras 10 linhas e com a função describe mostrar os formatos de cada coluna.

    Tabela fato_filme:

    ![Evidência](../Evidencias/Desafio/ETAPA4_4_-_TABELA_FATO_FILME.png)

    ![Evidência](../Evidencias/Desafio/ETAPA4_4_-_TABELA_FATO_FILME_2.png)

    Tabela dim_titulo:

    ![Evidência](../Evidencias/Desafio/ETAPA4_5_-_TABELA_DIM_TITULO.png)

    ![Evidência](../Evidencias/Desafio/ETAPA4_5_-_TABELA_DIM_TITULO_2.png)

    Tabela dim_tempo:

    ![Evidência](../Evidencias/Desafio/ETAPA4_6_-_TABELA_DIM_TEMPO.png)

    ![Evidência](../Evidencias/Desafio/ETAPA4_6_-_TABELA_DIM_TEMPO_2.png)

    Tabela dim_genero:

    ![Evidência](../Evidencias/Desafio/ETAPA4_7_-_TABELA_DIM_GENERO.png)

    ![Evidência](../Evidencias/Desafio/ETAPA4_7_-_TABELA_DIM_GENERO_2.png)

    Tabela bridge_genero:

    ![Evidência](../Evidencias/Desafio/ETAPA4_8_-_TABELA_BRIDGE_GENERO.png)

    ![Evidência](../Evidencias/Desafio/ETAPA4_8_-_TABELA_BRIDGE_GENERO_2.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa5"></a>

5. ... [Etapa 5 - Verificação Local dos arquivos parquet gerados](#Etapa5)

    Agora voltando no DBeaver, vai ser verificado os arquivos parquet gerados. No [script](sql\sql_verificacao.sql) primeiro é criado as tabelas com os arquivos parquet gerados pelo Glue e depois é feito a join de todas as tabelas com as informações contidas nelas.

    ![Evidência](../Evidencias/Desafio/ETAPA5_1_-_SCRIPT_SQL_VERIFICACAO.png)

    ![Evidência](../Evidencias/Desafio/ETAPA5_2_-_SCRIPT_SQL_PARTE_TABELA.png)

    E logo após isso é feito a verificação se os filmes que também serão analisados se estão presentes nas tabelas.

    ![Evidência](../Evidencias/Desafio/ETAPA5_3_-_SCRIPT_SQL_VERIFICACAO_FILMES.png)

[**Voltar ao Sumário**](#sumário)

<a id="Observacoes"></a>

6. ... [Observações](#Observacoes)

    I. As perguntas sofreram reformulações para um melhor direcionamento da análise.

    II. Para a utilização do Pyspark localmente foi instalado Java 11, o winutils - hadoop 3.0, pyspark 5.4.3 via pip install como mostrado no começo das etapas.

    III. Como dito durante as etapas, o script foi primeiro "debuggado" localmente, depois testado e adaptado para o ambiente do Glue.

    IV. Para a análise final vai ser utilizado apenas dados que respeitam os filtros que foram utilizados no endpoint discover que são: no mínimo 300 votos, com a votação média de 5, do gênero Terror e de idioma falado no filme inglês (Sprint 07).

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

4. ... [Anexo 4 - Versão DBeaver](#Anexo4)

    ![Evidência](../Evidencias/Desafio/ANEXO4_1_-_VERSAO_DBEAVER.png)

[**Voltar para Etapas**](#Etapas)

[**Voltar ao Sumário**](#sumário)

<a id="Anexo5"></a>

5. ... [Anexo 5 - Alguns arquivos gerados na fase de debugging](#Anexo5)

    ![Evidência](../Evidencias/Desafio/ANEXO5_1_-_ARQUIVOS_GERADOS_DEBUG.png)

[**Voltar para Etapas**](#Etapas)

[**Voltar ao Sumário**](#sumário)
