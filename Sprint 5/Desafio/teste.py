import boto3

# Especificando o profile certo que nesse caso é o boto3

session = boto3.Session(profile_name="boto3")

# Criacao do cliente para o s3

s3 = session.client('s3')

# bucket_name = 'desafio-sprint05teste123456'

# s3.create_bucket(Bucket = bucket_name)

response = s3.list_buckets()
print("Buckets disponíveis:", response['Buckets'])