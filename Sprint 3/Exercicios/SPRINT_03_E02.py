numeros = []

for i in range(0,3):
    numeros.append(i)

for numero in numeros:
    if numero % 2 == 0:
        print(f'Par: {numero}')
    else:
        print(f'Ímpar: {numero}')