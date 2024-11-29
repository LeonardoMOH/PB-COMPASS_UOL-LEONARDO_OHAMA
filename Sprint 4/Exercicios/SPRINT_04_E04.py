def calcular_valor_maximo(operadores, operandos) -> float:
    def calculo(pares_de_operando):
        (x, y), operador = pares_de_operando
        if operador == '+':
            return x + y
        elif operador == '-':
            return x - y
        elif operador == '/':
            return x / y
        elif operador == '*':
            return x * y
        elif operador == '%':
            return x % y
        else:
            raise ValueError(f"Operador inválido: {operador}")
    lista_total = list(map(calculo, zip(operandos, operadores)))
    return max(lista_total)

operadores = ['+', '-', '*', '/', '+']
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

print(calcular_valor_maximo(operadores, operandos))