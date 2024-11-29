from functools import reduce

lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]

def calcula_saldo(lancamentos) -> float:
    valores = map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)
    total = reduce(lambda x, y: x + y, valores)
    return total

calculo = calcula_saldo(lancamentos)

print(calculo)