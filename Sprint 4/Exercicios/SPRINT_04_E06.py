def maiores_que_media(conteudo:dict)->list:
    total = 0.0
    qtd_de_itens = 0

    for valor in conteudo.values():        
        total += valor        
        qtd_de_itens += 1        
    media = total / qtd_de_itens

    nova_lista = conteudo.copy()

    for chave, valor in list(nova_lista.items()):
        if media > valor:
            del nova_lista[chave]

    lista = sorted(nova_lista.items(), key = lambda item: item[1])
    return lista

conteudo = {

    'arroz': 4.99,

    'feijão': 3.49,

    'macarrão': 2.99,

    'leite': 3.29,

    'pão': 1.99

}

print(maiores_que_media(conteudo))