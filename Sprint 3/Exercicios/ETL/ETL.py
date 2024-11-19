with open('Sprint 3/Exercicios/ETL/actors.csv', 'r') as arquivo:
    primeira_leitura = arquivo.readlines()

# novo_csv = [separar_linhas.strip().split('\n') for separar_linhas in primeira_leitura]

# novo_csv = [separar_linhas.strip().split(',') for separar_linhas in primeira_leitura]

lista = []
for linha in primeira_leitura:
    linha = linha.strip()
    if '"' in linha:
        termo = []
        aspas_teste = False
        aspas = ""
        for aspas_for in linha:
            if aspas_for  == '"':
                aspas_teste = not aspas_teste
            elif aspas_for == ',' and not aspas_teste:
                termo.append(aspas)
                aspas = ""
            else:
                aspas += aspas_for
        termo.append(aspas)
        lista.append(termo)
    else:
        lista.append(linha.split(','))

# Etapa 1.1 = Maior número de filmes

print('Etapa 1.1 = Maior número de filmes:')

maior_numero_de_filmes = 0.0
ator_atriz = ''

for i, n in enumerate(lista[1:], start = 2):
    if float(n[2]) > float(maior_numero_de_filmes):
        maior_numero_de_filmes = int(n[2])
        ator_atriz = n[0]
    
print(f'O ator/atriz com maior número de filmes é {ator_atriz} com {maior_numero_de_filmes} filmes\n')

# Etapa 1.2 = Média de receita dos filmes

print('Etapa 1.2 = Média de receita dos filmes:')

receita_media = 0.0

for i, n in enumerate(lista[1:], start = 2):
    receita_media += float(n[5])
receita_media = receita_media/i

print(f'A média de receita bruta é: {receita_media:.2f} milhões de dólares\n')

# Etapa 1.3 = Média de bilheteria por filme

print('Etapa 1.3 = Média de bilheteria por filme:')

bilheteria = 0.0
ator_atriz_2 = ''

for i, n in enumerate(lista[1:], start = 2):
    if float(n[3]) > float(bilheteria):
        bilheteria = float(n[3])
        ator_atriz_2 = n[0]
    
print(f'O ator/atriz com a maior média de receita bruta por filme é {ator_atriz_2} com uma bilheteria de {bilheteria} milhões de dólares\n')

# Etapa 1.4 = #1 Filme

print('Etapa 1.4 = #1 Filme:')

quantidade = 1
lista_filme = lista
filme = lista_filme[1][4]

lista_filme.sort(key = lambda lista_filme: lista_filme[4]) 

for i, n in enumerate(lista_filme[1:], start = 2):
    if  n[4] == filme:
        quantidade += 1
    else:
        print(f'O filme {filme} aparece {quantidade} vez(es) no dataset')
        quantidade = 1
        filme = n[4]

print(f'O filme {filme} aparece {quantidade} vez(es) no dataset\n')
    
# Etapa 1.5 = #1 Lista decrescente Total Gross

print('Etapa 1.5 = #1 Lista decrescente Total Gross:')

nova_lista = lista

for i, n in enumerate(nova_lista[0:]):
        del n[2:6]

nova_lista.sort(key = lambda nova_lista: nova_lista[1], reverse = True) 

for i, n in enumerate(nova_lista[0:]):
    print(f'{n[0]} - {n[1]}')
