# Sumário

### Desafio:

1. [Script de Python para o Glue para processar o arquivo CSV](scripts/script_trusted_csv_glue.py)

2. [Script de Python para o Glue para processar o arquivo JSON](scripts/script_trusted_json.py)

3. [Script Python Auxiliar Local CSV](scripts/script_trusted_csv.py)

4. [Script Python Auxiliar Local JSON](scripts/script_trusted_json.py)

1. [Etapas](#etapas)

    I.    [Etapa 1 - ](#Etapa1)

    II.   [Etapa 2 - ](#Etapa2)

    III.  [Etapa 3 - ](#Etapa3)

    IV.   [Etapa 4 - ](#Etapa4)

    V.    [Etapa 5 - ](#Etapa5)

    VI.   [Etapa 6 - ](#Etapa6)
    
    VII.  [Observações](#Observacoes)

2. [Anexos](#anexos)

    I.    [Anexo 1 - Versão VSCode](#Anexo1)

    II.   [Anexo 2 - Versão Pyspark](#Anexo2)

    III.  [Anexo 3 - Versão Java](#Anexo3)

### README:

1. [README Principal](../../README.md)

2. [README Sprint 8](../README.md)

<a id="Etapas"></a>

# Etapas

Explicação do desenvolvimento da extração dos dados dos filmes pela API TMDB. Para o desenvolvimento foi utilizado o VSCode Version 1.96.4 (Release Date 16/01/2025), [winutils - hadoop 3.0 (GitHub de onde o arquivo foi baixado)](https://github.com/steveloughran/winutils/tree/master),Pyspark version 3.5.4, Java version "11.0.25" 2024-10-15  para mais informações: [Anexo 1 - Versão VSCode](#Anexo1), [Anexo 2 - Versão Pyspark](#Anexo2), [Anexo 3 - Versão Java](#Anexo3). 

<a id="Etapa1"></a>

1. ... [Etapa 1 - ](#Etapa1)
  
    ![Evidência](../Evidencias/Desafio/ETAPA1_1_-_ENDPOINT_DISCOVER.png)
    
    ![Evidência](../Evidencias/Desafio/ETAPA1_2_-_ENDPOINT_GENERO.png)

    ![Evidência](../Evidencias/Desafio/ETAPA1_3_-_ENDPOINT_CONFIG.png)

    ![Evidência](../Evidencias/Desafio/ETAPA1_4_-_ENDPOINT_ID.png)

    ![Evidência](../Evidencias/Desafio/ETAPA1_5_-_ENDPOINT_CREDITS.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa2"></a>

2. ... [Etapa 2 - ](#Etapa2)
    
    ![Evidência](../Evidencias/Desafio/ETAPA2_1_-_SCRIPT_PYTHON.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa3"></a>

3. ... [Etapa 3 - ](#Etapa3)

    ![Evidência](../Evidencias/Desafio/ETAPA3_1_-_SCRIPT_PYTHON.png)

    ![Evidência](../Evidencias/Desafio/ETAPA3_2_-_SCRIPT_PYTHON.png)

    ![Evidência](../Evidencias/Desafio/ETAPA3_3_-_SCRIPT_PYTHON.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa4"></a>

4. ... [Etapa 4 - ](#Etapa4)

    ![Evidência](../Evidencias/Desafio/ETAPA4_1_-_SCRIPT_PYTHON.png)

    ![Evidência](../Evidencias/Desafio/ETAPA4_2_-_SCRIPT_PYTHON.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa5"></a>

5. ... [Etapa 5 - Dockerfile, biblioteca requests](#Etapa5)

    ![Evidência](../Evidencias/Desafio/ETAPA5_1_-_DOCKER_LAYER_LAMBDA.png)

    ![Evidência](../Evidencias/Desafio/ETAPA5_2_-_DOCKER_LAYER_LAMBDA.png)

    ![Evidência](../Evidencias/Desafio/ETAPA5_3_-_LAYER_LAMBDA.png)

    ![Evidência](../Evidencias/Desafio/ETAPA5_4_-_LAYER_LAMBDA.png)

    ![Evidência](../Evidencias/Desafio/ETAPA5_5_-_CONFIGURACAO_LAMBDA.png)

[**Voltar ao Sumário**](#sumário)

<a id="Etapa6"></a>

6. ... [Etapa 6 - ](#Etapa6)

    ![Evidência](../Evidencias/Desafio/ETAPA6_1_-_LAMBDA.png)

    ![Evidência](../Evidencias/Desafio/ETAPA6_2_-_LAMBDA.png)

    ![Evidência](../Evidencias/Desafio/ETAPA6_3_-_LAMBDA.png)

    ![Evidência](../Evidencias/Desafio/ETAPA6_4_-_LAMBDA.png)

[**Voltar ao Sumário**](#sumário)

<a id="Observacoes"></a>

6. ... [Observações](#Observacoes)

    I. Possivelmente algumas perguntas feitas para o desafio final irão sofrer algumas alterações ao decorrer do Programa de Bolsas.

    II. Para a utilização do Pyspark localmente foi instalado Java 11, o winutils - hadoop 3.0, pyspark 5.4.3 via pip install como mostrado no começo das etapas e para os exercícios foi utilizado o Google Colab principalmente.

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
