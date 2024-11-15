import random

random_list = random.sample(range(500), 50)

random_list.sort()

mediana = (random_list[int((50 / 2)) - 1] + random_list[int((50 / 2))]) / 2
media = sum(random_list) / 50
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f'Media: {media}', end=", ")
print(f'Mediana: {mediana}', end=", ")
print(f'Mínimo: {valor_minimo}', end=", ")
print(f'Máximo: {valor_maximo}')