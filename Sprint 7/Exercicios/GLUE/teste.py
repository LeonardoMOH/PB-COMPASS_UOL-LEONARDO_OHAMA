import pandas as pd

file_path = "Sprint 7/Exercicios/GLUE/nomes.csv"
df = pd.read_csv(file_path)

# Comandos para verificar linhas duplicadas

duplicated_rows = df[df.duplicated(subset=['nome'], keep=False)]

duplicated_rows_sorted = duplicated_rows.sort_values(by='nome')

# Mostrar as linhas duplicadas no terminal

print("Linhas duplicadas baseadas na coluna 'nome':")
print(duplicated_rows_sorted)

# Número total de linhas duplicadas

print(f"Total de duplicatas: {len(duplicated_rows)}")
