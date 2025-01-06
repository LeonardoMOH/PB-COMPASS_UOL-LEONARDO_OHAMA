# FROM adicionando a ultima versao do python 3 na imagem

FROM python:3.13.0

# WORKDIR muda para o diretorio /app

WORKDIR /app

# Copia o arquivo sprint_06_script_python.py para a pasta /app/ do Docker

COPY ../scripts/sprint06_script_python.py /app/

# Instalacao das bibliotecas que serao utilizadas

RUN pip install --no-cache-dir boto3 pandas

# Comandos que serao executados no container
  
CMD ["python", "/app/sprint06_script_python.py"]