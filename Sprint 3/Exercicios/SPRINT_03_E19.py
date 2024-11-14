import random

random_list = random.sample(range(500), 50)

random_list.sort()

mediana = (random_list[24] + random_list[25]) / 2
media = sum(random_list) / 50
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f'Media: {media}', end=", ")
print(f'Mediana: {mediana}', end=", ")
print(f'Mínimo: {valor_minimo}', end=", ")
print(f'Máximo: {valor_maximo}', end="")