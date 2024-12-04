import hashlib

# Loop para o input que transforma a string do input em um hashcode do algoritmo SHA-1

while True:
    nome = input('Digite uma string: ')

    nome_hash = hashlib.sha1((nome.encode('utf-8'))).hexdigest()
    print(f'O hashcode SHA-1 da string é: {nome_hash}')

    # Loop para continuar o programa ou terminar o programa

    while True:

        continuar = input('Deseja continuar? Digite S para Sim e N para Não: ').upper()

        if continuar == 'S':
            break
        elif continuar == 'N':
            break
        else:
            print('Você não digitou S ou N')

    if continuar == 'N':
        break
