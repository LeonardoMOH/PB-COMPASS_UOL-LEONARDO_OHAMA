def conta_vogais(texto:str)-> int:
    vogal = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']    

    texto_vogais = list(filter(lambda letra: letra in vogal, texto))

    return len(texto_vogais)

quantidade_vogais = conta_vogais('aaaaaaaaaa')

print(quantidade_vogais)
