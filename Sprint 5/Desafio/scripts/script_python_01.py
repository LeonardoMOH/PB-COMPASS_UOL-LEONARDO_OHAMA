# import boto3

# # Especificando o profile certo que nesse caso é o boto3

# session = boto3.Session(profile_name="boto3")

# # Criacao do cliente para o s3

# s3 = session.client('s3')

# # Variaveis

# # Nome do bucket

# bucket_name = 'desafio-sprint05-awss3bucket'

# # Caminho dos arquivos que vai ser feito o upload

# csv_original_path = 'Sprint 5/Desafio/csv/APOSENTADOS_112024.csv'

# # Nome dos arquivos no bucket

# csv_original = 'APOSENTADOS_112024.csv'

# # Criacao do bucket no Norte da Virginia (us-east-1), o upload do arquivo do desafio e o download do dataset

# try:
#     s3.create_bucket(
#         Bucket = bucket_name
#     )
#     print(f'O Bucket {bucket_name} foi criado!')

#     s3.upload_file(csv_original_path,
#                    bucket_name,
#                    csv_original)
#     print(f'O arquivo {csv_original} teve um upload com sucesso.')

#     s3.download_file(bucket_name, 
#                      csv_original, 
#                      csv_original_path)
#     print(f'O arquivo {csv_original} teve um download com sucesso.')

# except Exception as e:
#     print(f'Erro ao criar o bucket {bucket_name}!')

###########################################################################
# Depois de rodar o segundo script Python rodar somente a parte de baixo se necessario criar o bucket novamente comentar a parte de baixo e rodar somente a parte acima

import boto3

session = boto3.Session(profile_name="boto3")

s3 = session.client('s3')

bucket_name = 'desafio-sprint05-awss3bucket'

arquivos_upload = [
    ('Sprint 5/Desafio/csv/APOSENTADOS_112024_NOVO.csv', 'csv/APOSENTADOS_112024_NOVO.csv'),
    ('Sprint 5/Desafio/csv/APOSENTADOS_112024_NOVO_FILTRADO.csv', 'csv/APOSENTADOS_112024_NOVO_FILTRADO.csv'),
    ('Sprint 5/Desafio/csv/APOSENTADOS_112024_VALOR_MAXIMO_FILTRADO.csv', 'csv/APOSENTADOS_112024_VALOR_MAXIMO_FILTRADO.csv'),
    ('Sprint 5/Desafio/csv/APOSENTADOS_112024_VALOR_MINIMO_FILTRADO.csv', 'csv/APOSENTADOS_112024_VALOR_MINIMO_FILTRADO.csv'),
    ('Sprint 5/Desafio/scripts/script_python_01.py', 'scripts/script_python_01.py'),
    ('Sprint 5/Desafio/scripts/script_python_02.py', 'scripts/script_python_02.py'),
    ('Sprint 5/Desafio/txt/lista_siglas.txt', 'txt/lista_siglas.txt'),
    ('Sprint 5/Desafio/txt/relatorio_dados.txt', 'txt/relatorio_dados.txt'),
    ('Sprint 5/Evidencias/Desafio/ETAPA1_1_-_BUSCA_DATASET.png', 'Evidencias/ETAPA1_1_-_BUSCA_DATASET.png'),
    ('Sprint 5/Evidencias/Desafio/ETAPA1_2_-_BUSCA_DATASET.png', 'Evidencias/ETAPA1_2_-_BUSCA_DATASET.png'),
    ('Sprint 5/Evidencias/Desafio/ETAPA2_1_-_ANALISE_DATASET.png', 'Evidencias/ETAPA2_1_-_ANALISE_DATASET.png'),
    ('Sprint 5/Evidencias/Desafio/ETAPA2_2_-_ANALISE_DATASET.png', 'Evidencias/ETAPA2_2_-_ANALISE_DATASET.png'),
    ('Sprint 5/Evidencias/Desafio/ETAPA2_3_-_ANALISE_DATASET.png', 'Evidencias/ETAPA2_3_-_ANALISE_DATASET.png'),
    ('Sprint 5/Evidencias/Desafio/ETAPA3_1_-_CONFIGURACAO_AWS.png', 'Evidencias/ETAPA3_1_-_CONFIGURACAO_AWS.png'),
    ('Sprint 5/Evidencias/Desafio/ETAPA3_2_-_CONFIGURACAO_AWS.png', 'Evidencias/ETAPA3_2_-_CONFIGURACAO_AWS.png'),
    ('Sprint 5/Evidencias/Desafio/ETAPA3_3_-_CONFIGURACAO_AWS.png', 'Evidencias/ETAPA3_3_-_CONFIGURACAO_AWS.png'),
    ('Sprint 5/Evidencias/Desafio/ETAPA4_1_-_SCRIPT_AWS.png', 'Evidencias/ETAPA4_1_-_SCRIPT_AWS.png'),
    ('Sprint 5/Evidencias/Desafio/ETAPA4_2_-_SCRIPT_AWS.png', 'Evidencias/ETAPA4_2_-_SCRIPT_AWS.png'),
    ('Sprint 5/Evidencias/Desafio/ETAPA4_3_-_SCRIPT_AWS.png', 'Evidencias/ETAPA4_3_-_SCRIPT_AWS.png'),
    ('Sprint 5/Evidencias/Desafio/ETAPA5_1_-_SCRIPT_TRATAMENTO.png', 'Evidencias/ETAPA5_1_-_SCRIPT_TRATAMENTO.png'),
    ('Sprint 5/Evidencias/Desafio/ETAPA5_2_-_SCRIPT_TRATAMENTO.png', 'Evidencias/ETAPA5_2_-_SCRIPT_TRATAMENTO.png'),
    ('Sprint 5/Evidencias/Desafio/ETAPA6_1_-_SCRIPT_TRATAMENTO_2.png', 'Evidencias/ETAPA6_1_-_SCRIPT_TRATAMENTO_2.png'),
    ('Sprint 5/Evidencias/Desafio/ETAPA7_1_-_SCRIPT_TRATAMENTO_3.png', 'Evidencias/ETAPA7_1_-_SCRIPT_TRATAMENTO_3.png'),
    ('Sprint 5/Evidencias/Desafio/ETAPA7_2_-_SCRIPT_TRATAMENTO_3.png', 'Evidencias/ETAPA7_2_-_SCRIPT_TRATAMENTO_3.png'),
    ('Sprint 5/Evidencias/Desafio/ETAPA7_3_-_SCRIPT_TRATAMENTO_3.png', 'Evidencias/ETAPA7_3_-_SCRIPT_TRATAMENTO_3.png'),
    ('Sprint 5/Evidencias/Desafio/ETAPA8_1_-_SCRIPT_PYTHON_AWS.png', 'Evidencias/ETAPA8_1_-_SCRIPT_PYTHON_AWS.png'),
    ('Sprint 5/Evidencias/Desafio/ETAPA8_2_-_SCRIPT_PYTHON_AWS.png', 'Evidencias/ETAPA8_2_-_SCRIPT_PYTHON_AWS.png'),
    ('Sprint 5/Evidencias/Desafio/ETAPA8_3_-_SCRIPT_PYTHON_AWS.png', 'Evidencias/ETAPA8_3_-_SCRIPT_PYTHON_AWS.png'),
    ('Sprint 5/Evidencias/Desafio/ANEXO1_-_VERSAO_VSCODE.png', 'Evidencias/ANEXO1_-_VERSAO_VSCODE.png'),
    ('Sprint 5/Evidencias/Desafio/ANEXO2_-_AWS_CLI.png', 'Evidencias/ANEXO2_-_AWS_CLI.png'),
    ('Sprint 5/Evidencias/Desafio/ANEXO3_-_AWS_TOOLKIT.png', 'Evidencias/ANEXO3_-_AWS_TOOLKIT.png'),
    ('Sprint 5/Evidencias/Desafio/ANEXO4_-_CSV_DADOS_TRATADOS.png', 'Evidencias/ANEXO4_-_CSV_DADOS_TRATADOS.png'),
    ('Sprint 5/Evidencias/Desafio/ANEXO5_-_CSV_DADOS_TRATADOS_E_FILTRADOS.png', 'Evidencias/ANEXO5_-_CSV_DADOS_TRATADOS_E_FILTRADOS.png'),
    ('Sprint 5/Evidencias/Desafio/ANEXO6_-_CSV_MINIMO.png', 'Evidencias/ANEXO6_-_CSV_MINIMO.png'),
    ('Sprint 5/Evidencias/Desafio/ANEXO7_-_CSV_MAXIMO.png', 'Evidencias/ANEXO7_-_CSV_MAXIMO.png'),
    ('Sprint 5/Evidencias/Desafio/ANEXO8_-_TXT_RELATORIO.png', 'Evidencias/ANEXO8_-_TXT_RELATORIO.png'),
    ('Sprint 5/Desafio/README.md', 'README.md')
]

try:
    for path, nome_arquivo_bucket in arquivos_upload:
        s3.upload_file(path, bucket_name, nome_arquivo_bucket)
        print(f'{nome_arquivo_bucket} teve um upload com sucesso.')

except Exception as e:
    print(f'Erro ao fazer upload dos arquivos: {e}')
