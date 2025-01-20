import os

animais = ['cachorro', 'gato', 'cavalo', 'peixe', 'golfinho',
            'tubarao', 'baleia', 'leão', 'papagaio', 'gorila',
            'chimpanzé', 'pinguim', 'urso', 'coelho', 'rinoceronte',
            'pato', 'tartaruga', 'girafa', 'crocodilo', 'canguru'
            ]

print(len(animais))

animais.sort()

arquivo = 'animais'
diretorio = 'Sprint 8/Exercicios/SPARK_BATCH/csv/'

os.makedirs(diretorio, exist_ok = True)

with open(f'{diretorio}{arquivo}.csv', 'w') as text_file:
    for x in animais:
        text_file.write(f'{x}\n')
        print(x)

print(f'O arquivo {arquivo} foi criado com sucesso!')