import boto3

# Especificando o profile certo que nesse caso é o boto3

session = boto3.Session(profile_name="boto3")

# Criacao do cliente para o s3

s3 = session.client('s3')

# Variaveis

# Nome do bucket

bucket_name = 'desafio-sprint05-teste123456'

# Caminho dos arquivos que vai ser feito o upload

csv_original_path = 'Sprint 5/Desafio/APOSENTADOS_112024.csv'
csv_tratado_path = 'Sprint 5/Desafio/APOSENTADOS_112024_NOVO.csv'
csv_resposta_path = 'Sprint 5/Desafio/APOSENTADOS_112024_NOVO_testefiltro.csv'
python_01_path = 'Sprint 5/Desafio/script_python_01.py'
python_02_path = 'Sprint 5/Desafio/script_python_02.py'

# Nome dos arquivos no bucket

csv_original = 'APOSENTADOS_112024.csv'
csv_tratado = 'APOSENTADOS_112024_NOVO.csv'
csv_resposta = 'APOSENTADOS_112024_NOVO_testefiltro.csv'
python_01 = 'script_python_01.py'
python_02 = 'script_python_02.py'

# Criacao do bucket no Norte da Virginia (us-east-1) e os uploads do arquivo do desafio

try:
    s3.create_bucket(
        Bucket = bucket_name
    )
    print(f'O Bucket {bucket_name} foi criado!')

    s3.upload_file(csv_original_path,
                   bucket_name,
                   csv_original)
    print(f'O arquivo {csv_original} teve um upload com sucesso.')

    s3.upload_file(csv_tratado_path,
                   bucket_name,
                   csv_tratado)
    print(f'O arquivo {csv_tratado} teve um upload com sucesso.')
    
    s3.upload_file(csv_resposta_path,
                   bucket_name,
                   csv_resposta)
    print(f'O arquivo {csv_resposta} teve um upload com sucesso.')
    
    s3.upload_file(python_01_path,
                   bucket_name,
                   python_01)
    print(f'O arquivo {python_01} teve um upload com sucesso.')
    
    s3.upload_file(python_02_path,
                   bucket_name,
                   python_02)
    print(f'O arquivo {python_02} teve um upload com sucesso.')

except Exception as e:
    print(f'Erro ao criar o bucket {bucket_name}!')

# response = s3.list_buckets()
# print("Buckets disponíveis:", response['Buckets'])
