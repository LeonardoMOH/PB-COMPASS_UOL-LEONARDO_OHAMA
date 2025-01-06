# Sumário

### Sprint 6:

1. [Resumo](#resumo)

2. [Exercícios](#exercícios)

    I.    [Exercício Lab AWS S3](#Exercício01)

    [index.html](../Sprint%205/Exercicios/index.html)

    [error.html](../Sprint%205/Exercicios/error.html)

    [nomes.csv](../Sprint%205/Exercicios/dados/nomes.csv)

    II.   [Exercício Lab AWS Athena](#Exercício02)

    III.  [Exercício Lab AWS Lambda](#Exercício03)

    IV.   [Exercício Lab AWS - Limpeza de recursos](#Exercício04)

3. [Evidências](#evidências)

4. [Certificados](#certificados)

### README:

1. [README Principal](../README.md)

2. [README Desafio](<Desafio/README.md>)

# Resumo

✍️‍ **AWS:** Nos cursos da AWS primeiro aprendemos alguns fundamentos para a análise de dados, como os 5 Vs do Big Data, Datalakes etc. Com os curso "Fundamentals of Analytics on AWS" que é dividido em duas partes. Depois tivemos curso que mostram os serviços da AWS, como: Redshift, Athena, Glue, EMR, Quicksight.

🎯 **Desafio** O desafio desta sprint é dividido em 5 partes, a primeira parte que é dessa sprint (Sprint 6). Essa primeira entrega consiste em fazer um script Python para executar dentro de um container do Docker para a ingestão de dados CSVs fornecidos (criar volume no Docker) e para isso é necessário utilizar a biblioteca boto3.

[**Voltar ao Sumário**](#sumário)

# Exercícios 🥋

<a id="Exercício01"></a>

### Exercício Lab AWS S3

Objetivo:


Explorar as capacidades do serviço AWS S3.  Nos passos que seguem, você será guiado pelas configurações necessárias para que um bucket do Amazon S3 funcione como hospedagem de conteúdo estático.



Antes de iniciar o laboratório é preciso realizar login no AWS Management Console, caso não esteja autenticado. Para tal, utilize o endereço https://academy-compass.awsapps.com/start#/, o qual permite acesso integrado com sua conta no Office365.



### Etapa 1: Criar um bucket


As instruções a seguir fornecem uma visão geral de como criar seus buckets para hospedagem de conteúdo estático:

No Console, busque pelo serviço S3.

Selecione Create bucket (Criar bucket).

Insira o Bucket name (Nome do bucket) (por exemplo, example.com).

Selecione a região onde você deseja criar o bucket. Escolha US East (N. Virginia) us-east-1.

Para aceitar as configurações padrão e criar o bucket, escolha Create (Criar).

![Resultado](<../Sprint%205/Evidencias/Exercicios/SPRINT_05_01.png>)

### Etapa 2: Habilitar hospedagem de site estático


Depois de criar um bucket, você pode habilitar a hospedagem de site estático nele. Os passos necessários são:



No Console, busque pelo serviço S3.

Na lista Buckets, escolha o nome do bucket para o qual você deseja habilitar a hospedagem de site estático.

Escolha Properties (Propriedades).

Em Static website hosting (Hospedagem estática de sites), escolha Edit (Editar).

Escolha Use this bucket to host a website (Usar este bucket para hospedar um site).

Em Static website hosting (Hospedagem estática de sites), escolha Enable (Ativar).

Em Index Document (Documento de índice), insira o nome do arquivo do documento de índice, que geralmente é index.html.

O nome do documento de índice diferencia letras maiúsculas de minúsculas e deve corresponder exatamente ao nome do arquivo do documento de índice HTML do qual você planeja fazer upload para o bucket do S3. Quando você configura um bucket para hospedagem de site, deve especificar um documento de índice. O Amazon S3 retorna esse documento de índice quando as solicitações são feitas para o domínio raiz ou alguma subpasta.



Para fornecer seu próprio documento de erros personalizado para erros da classe 4XX, em Error document (Documento de erros), insira o nome de arquivo do documento de erros personalizado.

O nome do documento de erro diferencia letras maiúsculas de minúsculas e deve corresponder exatamente ao nome do arquivo do documento de erro HTML do qual você planeja fazer upload para o bucket do S3. Se você não especificar um documento de erro personalizado e ocorrer um erro, o Amazon S3 retornará um documento de erro HTML padrão.



(Opcional) Se você quiser especificar regras avançadas de redirecionamento em Redirection rules (Regras de redirecionamento), use JSON para descrevê-las.

Por exemplo, você pode encaminhar solicitações condicionalmente de acordo com nomes de chave de objeto ou prefixos específicos na solicitação. Para obter mais informações, consulte Configurar regras de redirecionamento para usar redirecionamentos condicionais avançados.



Selecione Save changes.

O Amazon S3 permite a hospedagem estática de sites para seu bucket. Na parte inferior da página, em Static website hosting (Hospedagem estática de sites), você verá o endpoint do site do seu bucket.



Em Static website hosting (Hospedagem de sites estáticos), copie o endpoint informado.

O Endpoint é o endereço do site do Amazon S3 para o bucket.  Informe o endereço na barra de navegação de seu navegador para testar o resultado.



### Etapa 3: editar as configurações do Bloqueio de acesso público


Por padrão, o Amazon S3 bloqueia o acesso público à sua conta e aos seus buckets. Se quiser usar um bucket para hospedar um site estático, use estas etapas para editar as configurações de bloqueio de acesso público.



No Console, busque pelo serviço S3.

Escolha o nome do bucket configurado como um site estático.

Escolha Permissions (Permissões).

Em Block public access (bucket settings) (Bloqueio de acesso público (configurações de bucket), escolha Edit (Editar).

Desmarque Block all public access (Bloquear todo acesso público) e escolha Save changes (Salvar alterações).

O Amazon S3 desativa as configurações do bloqueio de acesso público para seu bucket. Para criar um site público e estático, você também pode ter que editar as configurações de Bloqueio de acesso público para sua conta antes de adicionar uma política de bucket. Se as configurações da conta para bloquear acesso público estiverem ativadas no momento, você verá uma observação em Block public access (bucket settings) (Bloqueio de acesso público (configurações de bucket)).



### Etapa 4: Adicionar política de bucket que torna o conteúdo do bucket publicamente disponível


Depois de editar as configurações do bloqueio de acesso público do S3, é possível adicionar uma política de bucket para conceder acesso público de somente leitura ao bucket. Ao conceder um acesso público de leitura, qualquer pessoa na Internet poderá acessar seu bucket.

Em Buckets, escolha o nome do seu bucket.

Escolha Permissions (Permissões).

Em Bucket Policy (Política de bucket), escolha Edit (Editar).

Para conceder acesso público de leitura ao site, copie a política de bucket a seguir e cole-a no Bucket policy editor (Editor de política de bucket).

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::Bucket-Name/*"
            ]
        }
    ]
}

![Resultado](<../Sprint%205/Evidencias/Exercicios/SPRINT_05_02.png>)

No JSON acima, substitua, na seção Resource, o valor de Bucket-Name para o nome do seu bucket.

Na política de bucket do exemplo anterior, Bucket-Name é um espaço reservado para o nome do bucket. Para usar essa política de bucket com seu próprio bucket, você deve atualizar esse nome para corresponder ao nome do seu bucket.



Selecione Save changes.

Uma mensagem é exibida indicando que a política de bucket foi adicionada com sucesso.

Se você vir um erro que diz Policy has invalid resource, confirme se o nome do bucket na política de bucket corresponde ao nome do seu bucket. Se você receber uma mensagem de erro e não puder salvar a política do bucket, verifique suas configurações de acesso público para confirmar que você permite acesso público ao bucket.



### Etapa 5: Configurar um documento de índice


Quando você habilita a hospedagem de sites estáticos para seu bucket, deve informar o nome do documento de índice (por exemplo, index.html). Naturalmente, o arquivo informado deverá estar presente no bucket para que a configuração tenha efeito.



Vamos aos passo para configuração do documento de índice:



Criar um arquivo local (sua máquina) com o nome index.html . O conteúdo do arquivo deverá ser (atente-se para o atributo href do link, pois ele deverá apontar para o arquivo CSV):

<html xmlns="http://www.w3.org/1999/xhtml" >
<head>
    <title>Home Page do meu WebSite - Tutorial de S3</title>
</head>
<body>
  <h1>Bem-vindo ao meu website</h1>
  <p>Agora hospedado em Amazon S3!</p>
  <a href="nome do arquivo CSV a ser baixado">Download CSV File</a> 
</body>
</html>
Salvar as alterações.

O nome do documento de índice deve corresponder exatamente ao nome do documento de índice que você inseriu na caixa de diálogo Hospedagem de site estático. O nome do documento de índice diferencia maiúsculas de minúsculas. Por exemplo, se você informou index.html na configuração do bucket, seu documento de índice também deverá ser index.html (e não Index.html, por exemplo).



No Console, busque pelo serviço S3.

Na lista Buckets, selecione o nome do bucket que você configurou hospedagem de conteúdo estático.

Para fazer upload do documento de índice para o bucket, siga um destes procedimentos:

Arraste e solte o arquivo de índice na listagem de buckets do console.

Escolha Upload (Fazer upload) e siga as instruções para escolher e fazer upload do arquivo de índice.

Crie uma pasta chamada dados e, após, faça upload do conteúdo do site (arquivo CSV) para ela.



### Etapa 6: configurar documento de erros


Depois de habilitar a hospedagem de sites estáticos para seu bucket, faça upload para o bucket de um arquivo HTML para notificação de erros.  Veja quais são os passos:



Crie um documento de erro com o nome 404.html.

Salve o arquivo localmente.

O nome do documento de erros diferencia maiúsculas e minúsculas e deve corresponder exatamente ao nome que você insere ao habilitar a hospedagem estática do site. Por exemplo, se você inserir 404.html como o nome do Error document (Documento de erro) na caixa de diálogo Static website hosting (Hospedagem de site estático), o nome de arquivo do documento de erro também deve ser 404.html.



No Console, busque pelo serviço S3.

Na lista Buckets, selecione o nome do bucket que você configurou hospedagem de conteúdo estático.

Para fazer upload do documento de erros para o bucket, siga um destes procedimentos:

Arraste e solte o arquivo de índice na listagem de buckets do console.

Escolha Upload (Fazer upload) e siga as instruções para escolher e fazer upload do arquivo de índice.



### Etapa 7: testar o endpoint do site


Depois de configurar a hospedagem de site estático para seu bucket, você pode testá-lo em seu navegador. Para tal, siga os passos a seguir:



No Console, busque pelo serviço S3.

Na lista Buckets, selecione o nome do bucket que você configurou hospedagem de conteúdo estático.

Escolha Properties (Propriedades).

Na parte inferior da página, em Static website hosting (Hospedagem estática de sites), escolha seu Bucket website endpoint (Endpoint de site do Bucket). Seu documento de índice é aberto em uma janela separada do navegador.

Agora você tem um site hospedado no Amazon S3. Esse site está disponível publicamente no endpoint de site do Amazon S3. Você pode também ter um domínio, como example.com, para exibir o conteúdo do site que criou. Neste caso, é preciso executar etapas adicionais.

![Resultado](<../Sprint%205/Evidencias/Exercicios/SPRINT_05_03.png>)



Referência
https://docs.aws.amazon.com/pt_br/AmazonS3/latest/userguide/HostingWebsiteOnS3Setup.html

[Solução Python Exercício 01](Exercicios/SPRINT_04_E01.py)

[Resultado Exercício 01](#Exercício01_1)

[**Voltar ao Sumário**](#sumário)

<a id="Exercício02"></a>

### Lab AWS Athena

Pré-requisitos
Ter executado o laboratório de AWS S3.

Antes de iniciar o laboratório é preciso realizar login no AWS Management Console, caso não esteja autenticado. Para tal, utilize o endereço https://academy-compass.awsapps.com/start#/, o qual permite acesso integrado com sua conta no Office365.





### Etapa 1: Configurar Athena


No Console, busque pelo serviço S3.

Verifique se o arquivo nomes.csv está no Bucket name (Nome do bucket) criado no laboratório de S3. Se não tiver, execute as seguintes etapas:

- Selecione Create bucket (Criar bucket)

- Insira o Bucket name (Nome do bucket).

- Selecione a região onde você deseja criar o bucket (US East (N. Virginia) us-east-1)

- Para aceitar as configurações padrão e criar o bucket, escolha Create (Criar).

- Para fazer upload do arquivo, siga um destes procedimentos:

-- Arraste e solte o arquivo na listagem de buckets do console.

-- Escolha Upload (Fazer upload) e siga as instruções para escolher e fazer upload do arquivo.

Realize download do arquivo nomes.csv (caso não tenha feito ainda).

Analise o arquivo descobrindo o nome e o tipo de dado de cada coluna.

De volta  ao Console AWS, crie uma pasta dentro do bucket chamada queries. O AWS Athena usará esta pasta para armazenar as consultas executadas.

Acesse o AWS Athena e clique em Explore the Query Editor (Explorar o editor de consultas).

No Athena, escolha View Settings (Visualizar configurações) para configurar um local para os resultados de consultas no Amazon S3.

Na guia Settings (Configurações), escolha Manage (Gerenciar).

Em Manage settings (Gerenciar configurações), faça um dos seguintes procedimentos:

Na caixa de texto Query result location (Localização dos resultados da consulta), insira o caminho para o bucket criado no Amazon S3 para resultados de consultas. Adicione o prefixo s3:// ao caminho. E aponte para a pasta queries criada.

Escolha Browse S3 (Navegar no S3), escolha o bucket do Amazon S3 que você criou na região atual e escolha Choose (Escolher).

Escolha Save (Salvar).

Selecione Editor para alternar para o editor de consultas.

![AWS Athena](<Evidencias/Exercicios/AWS_ATHENA/SPRINT_06_01_ATHENA.png>)

![AWS Athena](<Evidencias/Exercicios/AWS_ATHENA/SPRINT_06_02_ATHENA.png>)

### Etapa 2: Criar um banco de dados

À direita do painel de navegação, você pode usar o editor de consultas do Athena para inserir e executar as consultas e instruções.

Para criar um banco de dados denominado meubanco, insira a instrução CREATE DATABASE

CREATE DATABASE meubanco
Selecione Run (Executar) ou pressione Ctrl+ENTER.

Na lista Database (Banco de dados) à esquerda, escolha meubanco para torná-lo seu banco de dados atual.

![AWS Athena](<Evidencias/Exercicios/AWS_ATHENA/SPRINT_06_03_ATHENA.png>)

### Etapa 3: Criar uma tabela

Agora que você tem um banco de dados, pode criar uma tabela do Athena para ele. A tabela criada será baseada nos dados de log de exemplo do Amazon CloudFront, no local s3://athena-examples-myregion/cloudfront/plaintext/, em que myregion é a sua Região da AWS atual. Abaixo um exemplo:



CREATE EXTERNAL TABLE IF NOT EXISTS data.cloudfront_logs (
  `Date` DATE,
  Time STRING,
  Location STRING,
  Bytes INT,
  RequestIP STRING,
  Method STRING,
  Host STRING,
  Uri STRING,
  Status INT,
  Referrer STRING,
  ClientInfo STRING
  ) 
  ROW FORMAT DELIMITED
  FIELDS TERMINATED BY '\t'
  LINES TERMINATED BY '\n'
  LOCATION 's3://athena-examples-my-region/cloudfront/plaintext/';
Elabore a query para criar a tabela no banco de dados que você criou. Abaixo apresentamos um template para a estrutura de dados.

CREATE EXTERNAL TABLE IF NOT EXISTS <nome do banco de dados>.<nome da tabela> (
  <nome dos campos com o tipo de dados>
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
 'serialization.format' = ',',
 'field.delim' = ','
)
LOCATION <caminho do S3> 
Escolha Run.

Se a importação for bem-sucedida, você verá uma mensagem verde Completed (Concluído)

Algumas itens a observar para a atividade:



Definimos todos os campos no conjunto de dados e demos a eles um tipo apropriado.

Informamos ao Athena para usar o analisador LazySimpleSerDe CSV. Usamos esse analisador porque ele permite valores nulos para números. Ele não suporta valores entre aspas.

Informamos ao analisador que os campos são delimitados por vírgulas e que a primeira linha contém nomes de campos que podem ser ignorados.

Especificamos o local do arquivo CSV. Precisamos apenas fornecer a pasta, não o arquivo em si.

Teste os dados com a seguinte consulta, substituindo o nome dos campos, banco de dados e tabela pelos nomes que você criou anteriormente:

select nome from nomedobanco.nomedatabela where ano = 1999 order by total limit 15;
Crie uma consulta que lista os 3 nomes mais usados em cada década desde o 1950 até hoje.

![AWS Athena](<Evidencias/Exercicios/AWS_ATHENA/SPRINT_06_04_ATHENA.png>)

![AWS Athena](<Evidencias/Exercicios/AWS_ATHENA/SPRINT_06_05_ATHENA.png>)

<a id="Exercício03"></a>

### Lab AWS Lambda

Pré-requisitos


Faça a leitura do guia AWS de como criar sua primeira função do Lambda.

Ter executado os Laboratórios de S3 e Athena.

Ter o software Docker instalado em sua máquina.

Antes de iniciar o laboratório é preciso realizar login no AWS Management Console, caso não esteja autenticado. Para tal, utilize o endereço https://academy-compass.awsapps.com/start#/, o qual permite acesso integrado com sua conta no Office365.





### Etapa 1: Criar a função do Lambda


No console do AWS Lambda, selecione Criar uma função. Observação: o console só mostra esta página se não houver funções do Lambda criadas. Se já tiverem sido criadas funções, a opção será exibida a página Lambda > Funções.



Selecione Author from scratch (criar do zero)

Em Function name (nome da função), defina o nome da função. Em Runtime, escolha Python 3.9.

Para criar a função, selecione Create (Criar).

![AWS Lambda](<Evidencias/Exercicios/AWS_LAMBDA/SPRINT_06_01_LAMBDA.png>)

### Etapa 2: Construir o código


A função será criada e você será redirecionado para o editor de funções do console. Por padrão, será criado o arquivo nomeado lambda_function.py com o código abaixo:



import json
 
def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
Substitua # TODO implement pelo código que acessa o S3 e utiliza a biblioteca Numpy e Pandas para realizar a operação. Abaixo o código:

import json
import pandas
import boto3
 
 
def lambda_handler(event, context):
    s3_client = boto3.client('s3')
 
    bucket_name = '<coloque aqui o nome do seu bucket>'
    s3_file_name = 'dados/nomes.csv'
    objeto = s3_client.get_object(Bucket=bucket_name, Key=s3_file_name)
    df=pandas.read_csv(objeto['Body'], sep=',')
    rows = len(df.axes[0])
 
    return {
        'statusCode': 200,
        'body': f"Este arquivo tem {rows} linhas"
    }
Agora clique em Deploy para que a alteração do código seja realizada

Realize o teste da Lambda clicando em Test e escolhendo um nome de teste

Ao executar, o erro abaixo deve ser exibido:

Response
{
  "errorMessage": "Unable to import module 'lambda_function': No module named 'pandas'",
  "errorType": "Runtime.ImportModuleError",
  "requestId": "bd3ea45f-167d-420a-a926-0b6bd9634abe",
  "stackTrace": []
}
Este erro ocorre pois o serviço AWS Lambda não possui a biblioteca pandas. Precisamos de uma layer para importar estas bibliotecas necessárias a nossa Lambda.


![AWS Lambda](<Evidencias/Exercicios/AWS_LAMBDA/SPRINT_06_02_LAMBDA.png>)


### Etapa3: Criar uma Layer


Afinal, o que são Layers (camadas)? De acordo com a documentação, as camadas do Lambda fornecem um modo conveniente de empacotar bibliotecas e outras dependências que você pode usar com suas funções Lambda. O uso de camadas reduz o tamanho dos arquivos de implantação carregados e acelera a implantação do código.

Uma camada  é um arquivo compactado (zip) que pode conter código ou dados adicionais. Uma camada pode conter bibliotecas, um tempo de execução personalizado, dados ou arquivos de configuração. As camadas promovem o compartilhamento de código e a separação de responsabilidades para que você possa ater-se à escrita da lógica de negócios.

Quando você inclui uma camada em uma função lambda, o conteúdo é extraído para o diretório /opt no ambiente de execução



Agora você sabe o que é uma camada lambda, a próxima pergunta seria como criar uma?



É possível criar camadas usando o console da Lambda, a API do AWS Lambda, CloudFormation, ou AWS Serverless Application Model (AWS SAM). Aqui vamos usar o método do console da Lambda com comandos do prompt e arquivos no formato zip.

Usando esse método, estaremos instalando diretamente as bibliotecas python e suas dependências necessárias em pasta de um Conteiner Docker (sistema operacional Amazon Linux) e, em seguida, compactando-os para serem carregados na como camada à função Lambda.

Abaixo o passo a passo:



Crie uma pasta nova e nela crie um arquivo chamado Dockerfile. Vamos usar uma imagem de sistema operacional Linux específica da Amazon e instalar o python versão 3.9 e a ferramenta para fazer a compressão dos dados. O arquivo Dockerfile ficará assim:

FROM amazonlinux:2023
RUN yum update -y
RUN yum install -y \
python3-pip \
zip
RUN yum -y clean all


Vamos usar o arquivo construído acima para criar a imagem do Docker:

docker build -t amazonlinuxpython39 .


Agora, execute o comando abaixo na imagem do Docker para acessarmos o shell do container. O parâmetro -it é para sinalizar que queremos abrir imediatamente um shell:

docker run -it amazonlinuxpython39 bash


Então você verá o prompt de comando dizer bash-4.2# ou algo parecido. Agora precisamos criar a pasta que receberá as bibliotecas necessárias para a layer que criaremos. !!Importante!!: as bibliotecas devem estar dentro de uma pasta chamada python.

bash-4.2# cd ~
bash-4.2# mkdir layer_dir
bash-4.2# cd layer_dir/
bash-4.2# mkdir python
bash-4.2# cd python/
bash-4.2# pwd
No final você estará com a estrutura de diretórios assim: /root/layer_dir/python



Com a pasta criada, agora vamos baixar as bibliotecas e suas dependências para esta pasta python criada

bash-4.2# pip3 install pandas -t .
Se você navegar para a pasta python, deverá ver as bibliotecas instaladas. Agora, de volta ao layer_dir, vamos compactar o diretório python

Compacte todos esses arquivos em um arquivo chamado minha-camada-pandas.zip. Certifique-se que você está no diretório /root/layer_dir

bash-4.2# cd ..
bash-4.2# zip -r minha-camada-pandas.zip .


Copiar o zip do Container para a máquina local. Para tal, abra outra janela de terminal do seu SO e navegue até o diretório onde seu Dockerfile está. Inicialmente vamos descobrir o ID do Container Docker que está executando.

docker container ls


Com o ID do container listado, vamos copiar o arquivo para máquina local. Substitua  <id do container> pelo ID do container listado

docker cp <id do container>:/root/layer_dir/minha-camada-pandas.zip ./


De acordo com a AWS, se a camada possuir mais do que 10 MB, o ideal é fazer via S3. Então faça upload do arquivo minha-camada-pandas.zip para um bucket S3.

Agora temos a parte final onde carregamos o arquivo zip na Lambda para criar a camada. Retorne para o serviço AWS Lambda e no painel lateral, selecione Camadas

Clique no botão Criar uma camada

Dê o nome de PandasLayer, escolha a opção Fazer upload de um arquivo do Amazon S3. Em outra aba retorne ao S3, localize o arquivo minha-camada-pandas.zip que você carregou para o S3 anteriormente e copie a URL de objeto que está no S3, por exemplo: https://programa-bolsas-compass.s3.amazonaws.com/libs/minha-camada-pandas.zip. Retornando para a aba de criação da camada, cole a URL em Link do URL do Amazon S3

Escolha x86_64 em Arquiteturas compatíveis, em Tempos de execução compatíveis escolha Python 3.9

Clique em Criar

![AWS Lambda](<Evidencias/Exercicios/AWS_LAMBDA/SPRINT_06_03_LAMBDA.png>)

![AWS Lambda](<Evidencias/Exercicios/AWS_LAMBDA/SPRINT_06_04_LAMBDA.png>)

![AWS Lambda](<Evidencias/Exercicios/AWS_LAMBDA/SPRINT_06_05_LAMBDA.png>)

### Etapa 4: Utilizando a Layer

No menu, escolha Função e localize a função Lambda criada na Etapa 1

Localize o ícone Layers e clique nele ou vá até o rodapé da Lambda até a seção nomeada de Camadas

Clique em Adicionar uma camada

Escolha Custom Layers (Camadas personalizadas), localize a camada e a versão criada na etapa anterior.

Clique em Adicionar

Agora execute novamente o código criado com o Test definido anteriormente. Deve ser retornado algo assim no Response:

{
  "statusCode": 200,
  "body": "Este arquivo tem 1825433 linhas"
}
Dica: Provavelmente será necessário aumentar o tempo limite e o tamanho da memória da Lambda.

![AWS Lambda](<Evidencias/Exercicios/AWS_LAMBDA/SPRINT_06_06_LAMBDA.png>)

![AWS Lambda](<Evidencias/Exercicios/AWS_LAMBDA/SPRINT_06_07_LAMBDA.png>)

![AWS Lambda](<Evidencias/Exercicios/AWS_LAMBDA/SPRINT_06_08_LAMBDA.png>)

![AWS Lambda](<Evidencias/Exercicios/AWS_LAMBDA/SPRINT_06_09_LAMBDA.png>)

![AWS Lambda](<Evidencias/Exercicios/AWS_LAMBDA/SPRINT_06_10_LAMBDA.png>)

<a id="Exercício04"></a>

### Lab AWS - Limpeza de recursos

Após concluir todas as etapas dos laboratórios e de colher as evidências/códigos para repassar ao monitor (a), você deve realizar a limpeza do que foi criado, para não incorrer em custos desnecessários.

Lembre-se de:

Excluir os arquivos usados/gerados durante os laboratórios do S3

# Certificados

[Amazon EMR Getting Started](<Certificados/Amazon EMR Getting Started.pdf>)

![Amazon EMR Getting Started](<Certificados/Amazon EMR Getting Started.png>)

[Amazon QuickSight Getting Started](<Certificados/Amazon QuickSight Getting Started.pdf>)

![Amazon QuickSight Getting Started](<Certificados/Amazon QuickSight Getting Started.png>)

[AWS Glue Getting Started](<Certificados/AWS Glue Getting Started.pdf>)

![AWS Glue Getting Started](<Certificados/AWS Glue Getting Started.png>)

[Best Practices for Data Warehousing with Amazon RedShift (Portuguese)](<Certificados/Best Practices for Data Warehousing with Amazon RedShift (Portuguese).pdf>)

![Best Practices for Data Warehousing with Amazon RedShift (Portuguese)](<Certificados/Best Practices for Data Warehousing with Amazon RedShift (Portuguese).png>)

[Nocoes Basicas de Analytics na AWS Parte 1 (Portugues)](<Certificados/Nocoes Basicas de Analytics na AWS Parte 1 (Portugues).pdf>)

![Nocoes Basicas de Analytics na AWS Parte 1 (Portugues)](<Certificados/Nocoes Basicas de Analytics na AWS Parte 1 (Portugues).png>)

[Fundamentos de Analytics na AWS Parte 2 (Portugues)](<Certificados/Fundamentos de Analytics na AWS Parte 2 (Portugues).pdf>)

![Fundamentos de Analytics na AWS Parte 2 (Portugues)](<Certificados/Fundamentos de Analytics na AWS Parte 2 (Portugues).png>)

[Getting Started with Amazon Redshift (Portuguese)](<Certificados/Getting Started with Amazon Redshift (Portuguese).pdf>)

![Getting Started with Amazon Redshift (Portuguese)](<Certificados/Getting Started with Amazon Redshift (Portuguese).png>)

[Introduction to Amazon Athena (Portuguese)](<Certificados/Introduction to Amazon Athena (Portuguese).pdf>)

![Introduction to Amazon Athena (Portuguese)](<Certificados/Introduction to Amazon Athena (Portuguese).png>)

[Serverless Analytics (Portuguese)](<Certificados/Serverless Analytics (Portuguese).pdf>)

![Serverless Analytics (Portuguese)](<Certificados/Serverless Analytics (Portuguese).png>)

[**Voltar ao Sumário**](#sumário)