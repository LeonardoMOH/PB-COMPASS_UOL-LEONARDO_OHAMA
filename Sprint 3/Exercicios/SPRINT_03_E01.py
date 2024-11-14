from datetime import datetime

nome = "Mario"
idade = 30
ano_atual = datetime.now().year
ano_100 = ano_atual + (100 - idade)

print(f'{ano_100}')