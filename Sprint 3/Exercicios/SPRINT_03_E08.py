lista = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for i, n in enumerate(lista):
    a = lista[i]
    split = list(a)
    split_reverse = split[::-1]

    if split == split_reverse:
        print(f'A palavra: {n} é um palíndromo')
    else:
        print(f'A palavra: {n} não é um palíndromo')