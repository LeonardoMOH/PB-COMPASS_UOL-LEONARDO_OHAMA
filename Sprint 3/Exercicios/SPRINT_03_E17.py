def funcao(n):
    divisao = len(n) // 3
    a = n[:divisao]
    b = n[divisao:divisao*2]
    c = n[divisao*2:]

    return f"{a} {b} {c}"

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(funcao(lista))