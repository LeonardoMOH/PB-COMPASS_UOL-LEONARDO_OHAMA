import pandas as pd

import csv

from datetime import date

import os

# Essas linhas tentei utilizar, porem ocorreu erro no "encoding"

# arquivo = "APOSENTADOS_112024.csv"

# df = pd.read_csv(arquivo, sep = ",")

# Nessa operacao foi feita a abertura do arquivo para ler o tipo de enconding predominante no arquivo

# import chardet

# with open('Sprint 5/Desafio/APOSENTADOS_112024.csv', "rb") as file:
#     result = chardet.detect(file.read(1000))
#     print(result)

# Criacao de pastas

os.makedirs('Sprint 5/Desafio/Video/txt', exist_ok = True)
os.makedirs('Sprint 5/Desafio/Video/csv', exist_ok = True)
os.makedirs('Sprint 5/Desafio/Video/scripts', exist_ok = True)

# Abertura do arquivo CSV

with open(
    'Sprint 5/Desafio/APOSENTADOS_112024.csv', 
    "r", 
    encoding="ISO-8859-1"
) as arquivo:
    df = pd.read_csv(arquivo, 
                     sep = ";",
                     names = ['Nome', 
                              'CPF', 
                              'Matricula', 
                              'Orgao', 
                              'Sigla Orgao', 
                              'Orgao vinculacao', 
                              'Carga emprego', 
                              'Classe', 
                              'Padrao', 
                              'Referencia', 
                              'Nivel', 
                              'Tipo aposentadoria', 
                              'Fund legal aposentadoria', 
                              'Portaria aposentadoria', 
                              'Dt ocorrencia inatividade', 
                              'Nome ocorrencia', 
                              'Dt ingresso servico publico', 
                              'Valor aposentadoria']
                     )

# Tratamento de dados

# Tirando espacos

df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

# Mudando os valores para Desconhecido na coluna "Portaria aposentadoria"

df.loc[df['Portaria aposentadoria'] == '', 'Portaria aposentadoria'] = 'Desconhecido'

# Mudando os valores da aposentadoria que estao em virgula para ponto

df['Valor aposentadoria'] = df['Valor aposentadoria'].str.replace('.', '', regex = False).str.replace(',', '.', regex = False).astype(float)

# Mudando as datas

df['Dt ocorrencia inatividade'] = df['Dt ocorrencia inatividade'].astype(str).apply(lambda x: '0' + x if len(x) == 7 else x)
df['Dt ocorrencia inatividade'] = pd.to_datetime(df['Dt ocorrencia inatividade'], format='%d%m%Y')
df['Dt ocorrencia inatividade'] = df['Dt ocorrencia inatividade'].dt.strftime('%d-%m-%Y')

df['Dt ingresso servico publico'] = df['Dt ingresso servico publico'].astype(str).apply(lambda x: '0' + x if len(x) == 7 else x)
df['Dt ingresso servico publico'] = pd.to_datetime(df['Dt ingresso servico publico'], format='%d%m%Y')
df['Dt ingresso servico publico'] = df['Dt ingresso servico publico'].dt.strftime('%d-%m-%Y')

# Soma das aposentadorias do csv filtrado

def soma_aposentadoria(dataframe):
    soma = dataframe.groupby('Tipo aposentadoria', as_index = False)['Valor aposentadoria'].sum(numeric_only = True)
    return soma

# Media das aposentadorias do csv filtrado

def media_aposentadoria(dataframe):
    media = dataframe['Valor aposentadoria'].mean()
    return media

# Valor maximo da aposentadoria do csv filtrado

def max_aposentadoria(dataframe):
    max = dataframe['Valor aposentadoria'].max()
    return max

def max_aposentadoria_csv(dataframe):
    max_csv = dataframe.sort_values(by = 'Valor aposentadoria', ascending = False)
    return max_csv

# Valor minimo da aposentadoria do csv filtrado

def min_aposentadoria(dataframe):
    min = dataframe['Valor aposentadoria'].min()
    return min

def min_aposentadoria_csv(dataframe):
    min_csv = dataframe.sort_values(by = 'Valor aposentadoria', ascending = True)
    return min_csv

# Retorna o dataframe somente com os valores por tipo de aposentadoria

def tipo_aposentadoria(valor, df):
    if valor == 1:
        df_temp = df[df['Tipo aposentadoria'] == 'VOLUNTARIA']
    elif valor == 2:
        df_temp = df[df['Tipo aposentadoria'] == 'COMPULSORIA']
    elif valor == 3:
        df_temp = df[df['Tipo aposentadoria'] == 'APOSENTADORIA POR INVALIDEZ']
    elif valor == 4:
        df_temp = df[df['Tipo aposentadoria'] == 'INCAPACIDADE']
    elif valor == 0:
        return df
    return df_temp

# Filtrando valores pelo Orgao = INSS ou MS e valor de aposentadoria de mais de 7000 reais e no final gerar CSVs com a linha máxima e mínima

# Criacao de uma lista separada para o input para esse caso, como dito anteriomente sera utilizado INSS ou MS para os orgaos e o valor da aposentadoria de no minimo 7000 reais

sigla_nomes = df.groupby('Sigla Orgao', as_index = False).sum()['Sigla Orgao']
with open('Sprint 5/Desafio/txt/lista_siglas.txt', 'w') as text_file:
    for siglas in sigla_nomes:   
        text_file.write(f'{siglas}\n')

while True:
    sigla_1 = input('Escolha a Sigla do Orgao: ').upper()
    if sigla_1 in df['Sigla Orgao'].str.upper().values:
        sigla_2 = input('Escolha uma segunda Sigla do Orgao: ').upper()
        if sigla_2 in df['Sigla Orgao'].str.upper().values:
            valor_apos = input('Escolha o mínimo valor da aposentadoria a ser filtrada: ')
            try:
                valor_apos = float(valor_apos)
                if valor_apos < 1:
                    print('Digite um valor numérico positivo.')
                break
            except ValueError:
                print('Digite um valor numérico.')
        else:
            print('Digite uma sigla valida!')
    else:
        print('Digite uma sigla valida!')

df_filtrado = df[((df['Sigla Orgao'] == sigla_1) | (df['Sigla Orgao'] == sigla_2)) & (df['Valor aposentadoria'] > valor_apos)]

# Loop para gerar o arquivo tratado com restricoes nos tipos de aposentadoria

while True:
    valor = input('''
Tipos de aposentadoria
Digite:
1 para Voluntaria,
2 para Compulsoria,
3 para Invalidez,
4 para Incapacidade e
0 para terminar a consulta e caso nao selecionado nenhuma das opcoes anteriores sera feito um relatorio com todas as opcoes: '''
                  )

    if valor.isdigit():
        valor = int(valor)
        if valor in [1, 2, 3, 4]:
            break
        elif valor == 0:
            break
        else:
            print('Digite uma das opcoes')
    else:
        print('Digite uma das opcoes')

# Chamada da funcao e a criacao do dataframe filtrado
        
df_resultado = tipo_aposentadoria(valor, df_filtrado)

# Loop para filtrar a data inserida

while True:
    dia = int(input('Escolha até qual data deve ser gerado o CSV: '))
    if dia < 1 or dia > 31:
        print("Insira um dia válido entre 1 e 31.")
        continue

    df_resultado_copia = df_resultado.copy()
    df_resultado_copia['Dt ocorrencia inatividade'] = pd.to_datetime(df_resultado_copia['Dt ocorrencia inatividade'], format='%d-%m-%Y')
    df_resultado_2 = df_resultado_copia[df_resultado_copia['Dt ocorrencia inatividade'].dt.day <= dia]
    df_resultado_copia = df_resultado.copy()
    df_resultado_2['Dt ocorrencia inatividade'] = df_resultado_2['Dt ocorrencia inatividade'].dt.strftime('%d-%m-%Y')

    break

df_resultado_2.to_csv('Sprint 5/Desafio/csv/APOSENTADOS_112024_NOVO_FILTRADO.csv', 
          index = False, 
          quoting=csv.QUOTE_MINIMAL)

# Utilizacao das funcoes para o relatorio txt

nome_arquivo = 'APOSENTADOS_112024.csv'
dia_atual = date.today().strftime("%d-%m-%Y")

linha, coluna = df.shape
linha_filt, coluna_filt = df_filtrado.shape
soma = soma_aposentadoria(df_filtrado)
media = media_aposentadoria(df_filtrado)
max = max_aposentadoria(df_filtrado)
min = min_aposentadoria(df_filtrado)

# Relatorio txt dos dados

with open('Sprint 5/Desafio/txt/relatorio_dados.txt', 'w') as text_file:
    text_file.write(f'Relatório do arquivo {nome_arquivo} feito no dia {dia_atual}\n\n'
                    f'Foram filtrados os orgãos {sigla_1} ou {sigla_2} e as aposentadorias acima de {valor_apos} reais\n\n'
                    f'O número de linhas do arquivo original é {linha} e o número de colunas é {coluna}\n'
                    f'O número de linhas do arquivo tratado e filtrado é {linha_filt} e o número de colunas é {coluna_filt}\n'
                    f'O máximo valor de aposentadoria é: {max} reais\n'
                    f'O mínimo valor de aposentadoria é: {min} reais\n'
                    f'A média do valor de aposentadoria é: {media:.2f} reais\n\n'
                    f'A soma das aposentadorias é:\n {soma}'
                    )

# Linha com o valor maximo da aposentadoria

linha_max = max_aposentadoria_csv(df_filtrado).head(1)
linha_max.to_csv('Sprint 5/Desafio/csv/APOSENTADOS_112024_VALOR_MAXIMO_FILTRADO.csv', 
          index = False, 
          quoting=csv.QUOTE_MINIMAL)

# Linha com o valor minimo da aposentadoria

linha_min = min_aposentadoria_csv(df_filtrado).head(1)
linha_min.to_csv('Sprint 5/Desafio/csv/APOSENTADOS_112024_VALOR_MINIMO_FILTRADO.csv', 
          index = False, 
          quoting=csv.QUOTE_MINIMAL)

# Novo arquivo com os tratamento de dados

df.to_csv('Sprint 5/Desafio/csv/APOSENTADOS_112024_NOVO.csv', 
          index = False, 
          quoting=csv.QUOTE_MINIMAL)
