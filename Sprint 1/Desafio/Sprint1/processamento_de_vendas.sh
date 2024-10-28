#!/bin/bash

: 'Registra a data e hora que o programa começa a ser executado em três variáveis'

DATA_ARQUIVO=$(date +%Y%m%d)
DATA_REL=$(date +%Y/%m/%d)
HORA=$(date +%T)
DATA_ATUAL=$(date +%d/%m/%Y)

: 'Cria o diretório ecommerce e move os arquivo de dados_de_vendas e processamento_de_dados para esse diretório'

mkdir -p ecommerce
mv dados_de_vendas.csv ecommerce/

: 'Estas linhas criam uma pasta de Vendas e um subdiretório Backup no diretório de Vendas, depois copia o dado_de_vendas.csv e renomeia com o prefixo backup na pasta de Backup.'

mkdir -p ecommerce/vendas
mkdir -p ecommerce/vendas/backup
cd ecommerce/
cp dados_de_vendas.csv backup-dados-$DATA_ARQUIVO.csv
mv backup-dados-$DATA_ARQUIVO.csv vendas/backup
mv dados_de_vendas.csv vendas/

: 'Estas linhas vão fazer o relatório em txt.'

cd vendas/
echo "Relatório do dia" $DATA_REL $HORA > relatorio$DATA_ARQUIVO.txt

: 'Ordena pelas datas em ordem crescente e cria um arquivo auxiliar, com uma coluna para ajudar na ordenação das datas (YYYYMMDD)'

awk -F ',' 'BEGIN{OFS=","} NR==1 {print $0} NR>1  {split($5,a,"/"); $6=a[3]a[2]a[1]; print $0}' dados_de_vendas.csv > dados_de_vendas_ord.csv
sort -t ',' -k6,6n dados_de_vendas_ord.csv > dados_de_vendas_ord2.csv && mv dados_de_vendas_ord2.csv dados_de_vendas_ord.csv

: 'Pega a 2 linha, porque a 1 linha contém o cabeçalho'

echo "Primeiro item comprado: " >> relatorio$DATA_ARQUIVO.txt
awk -F ',' 'BEGIN{OFS=","} NR==2 {print $1,$2,$3,$4,$5}' dados_de_vendas_ord.csv >> relatorio$DATA_ARQUIVO.txt

: 'Pega a última linha da lista ordenada'

echo "Último item comprado: " >> relatorio$DATA_ARQUIVO.txt
awk -F ',' 'BEGIN{OFS=","} END {print $1,$2,$3,$4,$5}' dados_de_vendas_ord.csv >> relatorio$DATA_ARQUIVO.txt

: 'Pega todos os itens fora o cabeçalho e exclui as linhas diferentes'

echo -n "Número de itens diferentes: " >> relatorio$DATA_ARQUIVO.txt
cut -d ',' -f2 dados_de_vendas.csv | tail -n +2 | sort  | uniq -c  | wc -l >> relatorio$DATA_ARQUIVO.txt

: 'Pega as 10 primeiras linhas do arquivo tirando o cabeçalho'

echo "Primeiras 10 linhas do arquivo backup do dia $DATA_ATUAL" >> relatorio$DATA_ARQUIVO.txt
tail -n +2 dados_de_vendas.csv | head -n 10 >> relatorio$DATA_ARQUIVO.txt

rm dados_de_vendas_ord.csv

: 'Move o arquivo relatório para vendas/backup'

mv relatorio$DATA_ARQUIVO.txt backup/

: 'Cria um arquivo zip do backup dos dados e remove o arquivo de dados'

cd backup/
zip -r backup-dados-$DATA_ARQUIVO.zip backup-dados-$DATA_ARQUIVO.csv
rm backup-dados-$DATA_ARQUIVO.csv
cd ..
rm dados_de_vendas.csv
