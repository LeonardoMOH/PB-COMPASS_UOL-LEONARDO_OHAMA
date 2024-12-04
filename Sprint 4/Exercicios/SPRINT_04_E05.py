with open('Sprint 4/Exercicios/estudantes.csv', 'r') as arquivo:
    primeira_leitura = arquivo.readlines()

arquivo = [separar_linhas.strip().split(',') for separar_linhas in primeira_leitura]

nova_lista = []

for n in arquivo:
    nome = n[0]

    notas = list(map(int, n[1:6]))

    notas = sorted(notas, reverse = True)

    n1 = notas[0]
    n2 = notas[1]
    n3 = notas[2]
    media = round((n1 + n2 + n3) / 3, 2)

    nova_lista.append([nome, n1, n2, n3, media])

nova_lista = sorted(nova_lista, key = lambda x: x[0])

for n in nova_lista:
    print(f'Nome: {n[0]} Notas: [{n[1]}, {n[2]}, {n[3]}] Média: {n[4]}')
