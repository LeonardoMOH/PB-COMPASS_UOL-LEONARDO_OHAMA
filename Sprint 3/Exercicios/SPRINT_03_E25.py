class Aviao:
    cor = 'azul'

    def __init__(self, modelo, velocidade_maxima, cor, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = cor
        self.capacidade = capacidade

    def __str__(self):
        return f'O avião de modelo {self.modelo} possui uma velocidade máxima de {self.velocidade_maxima}, capacidade para {self.capacidade} passageiros e é da cor {self.cor}'


modelo_a = Aviao('BOIENG456', 150, 'azul', 400)

modelo_b = Aviao('Embraer Praetor', 600, 'azul', 14)

modelo_c = Aviao('Antonov An-2', 258, 'azul', 12)

lista = [modelo_a, modelo_b, modelo_c]

for i in lista:
    print(i)
