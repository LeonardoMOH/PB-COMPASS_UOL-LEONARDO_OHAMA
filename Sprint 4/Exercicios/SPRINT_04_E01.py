with open('Sprint 4/Exercicios/number.txt', 'r') as arquivo:
    primeira_leitura = arquivo.read().splitlines()

arquivo = [separar_linhas.strip() for separar_linhas in primeira_leitura]

arquivo = list(map(int, arquivo))

pares = list(map(lambda x: x if x % 2 == 0 else None, arquivo))

pares_filter = list(filter(None, pares))

pares_sorted = sorted(pares_filter, reverse = True)

pares_maiores = pares_sorted[:5]

print(pares_maiores)

pares_somados = sum(pares_maiores)

print(pares_somados)