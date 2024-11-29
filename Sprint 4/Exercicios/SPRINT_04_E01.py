lista = [8000,7998,7996,7994,7994]

pares = list(map(lambda x: x if x % 2 == 0 else None, lista))

pares_filter = list(filter(None, pares))

pares_sorted = sorted(pares_filter, reverse = True)

pares_maiores = pares_sorted[:5]

print(pares_maiores)

pares_somados = sum(pares_maiores)

print(pares_somados)