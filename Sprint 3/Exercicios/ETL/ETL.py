with open('Sprint 3/Exercicios/ETL/actors.csv', 'r') as arquivo:
    primeira_leitura = arquivo.readlines()

novo_csv = [separar_linhas.strip().split(',') for separar_linhas in primeira_leitura]

maior_numero_de_filmes = 0.0

for i, n in enumerate(novo_csv[1:], start = 2):
    if float(n[2]) > float(maior_numero_de_filmes):
        maior_numero_de_filmes = float(n[2])
    
print(maior_numero_de_filmes)