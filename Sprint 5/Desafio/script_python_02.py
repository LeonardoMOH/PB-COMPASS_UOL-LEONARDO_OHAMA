import pandas as pd

import csv

# Essas linhas tentei utilizar, porem ocorreu erro no "encoding"

# arquivo = "APOSENTADOS_112024.csv"

# df = pd.read_csv(arquivo, sep = ",")

# Nessa operacao foi feita a abertura do arquivo para ler o tipo de enconding predominante no arquivo

# import chardet

# with open('Sprint 5/Desafio/APOSENTADOS_112024.csv', "rb") as file:
#     result = chardet.detect(file.read(1000))
#     print(result)

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

df_obj = df.select_dtypes('object')
df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())

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

# Opcao para que dados o usuario quer que seja filtrado

# while True:
    
#     break

# Filtrando valores pelo Orgao = INSS e valor de aposentadoria de mais de 7000 reais

df_filtrado = df[(df['Sigla Orgao'] == 'INSS') | (df['Sigla Orgao'] == 'MS') & (df['Valor aposentadoria'] >= 7000)]

# Funcoes

def soma_por_aposentadoria(dataframe):
    tipos = dataframe.groupby('Tipo aposentadoria', as_index = False).sum()
    return tipos

def media_aposentadoria(dataframe):
    media = dataframe['Valor aposentadoria'].mean()
    return media

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

while True:
    valor = input('Tipos de aposentadoria\nDigite:\n1 para Voluntaria,\n2 para Compulsoria,\n3 para Invalidez,\n4 para Incapacidade e\n0 para terminar a consulta: ')

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
        
df_resultado = tipo_aposentadoria(valor, df_filtrado)

df_resultado.to_csv('Sprint 5/Desafio/APOSENTADOS_112024_NOVO_testefiltro.csv', 
          index = False, 
          quoting=csv.QUOTE_MINIMAL)

# Novo arquivo com os tratamento de dados

df.to_csv('Sprint 5/Desafio/APOSENTADOS_112024_NOVO.csv', 
          index = False, 
          quoting=csv.QUOTE_MINIMAL)

