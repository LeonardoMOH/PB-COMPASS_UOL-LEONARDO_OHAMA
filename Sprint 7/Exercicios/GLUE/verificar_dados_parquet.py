import pandas as pd

df = pd.read_parquet("Sprint 7/Exercicios/GLUE/part-00000-5d1b072a-81b7-46a0-bc5e-a892a97cde0d-c000.snappy.parquet")
print(df.head())
