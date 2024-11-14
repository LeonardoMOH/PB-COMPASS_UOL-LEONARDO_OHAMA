## constantes = (1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

def todos_params(*args, **kwargs):
    for i, termo in enumerate (args):
        print(f'{termo}')
    for chave, valor in kwargs.items():
        print(f'{valor}')   
    

todos_params(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)