class Calculo:
    
    def __init__(self):
        pass


    def soma(self, x, y):
        z = x + y
        return print(f'Somando: {x}+{y} = {z}')
    
    
    def sub(self, x, y):
        z = x - y
        return print(f'Subtraindo: {x}-{y} = {z}')

x = 4
y = 5

calculo = Calculo()

calculo.soma(x, y)

calculo.sub(x, y)