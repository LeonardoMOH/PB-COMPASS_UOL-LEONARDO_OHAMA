import random
import time
import names

random.seed(40)

qtd_nomes_unicos = 3000

qtd_nomes_aleatorios = 10000000

aux = []

for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios")

dados = []

for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))