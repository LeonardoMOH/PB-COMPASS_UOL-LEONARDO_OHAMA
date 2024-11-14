lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_2 = []

def my_map(list, f):
    for i in list:
        f(i)
    print(lista_2)


def potencia(n):
    a = n ** 2
    lista_2.append(a)


my_map(lista, potencia)