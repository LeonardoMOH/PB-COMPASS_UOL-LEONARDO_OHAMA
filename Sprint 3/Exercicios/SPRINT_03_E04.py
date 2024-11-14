for x in range(1, 101):
    teste_primo = True
    if x <= 1:
        teste_primo = False
    else:
        for i in range(2, int(x / 2) + 1):
            if x % i == 0:
                teste_primo = False
                break
            else:
                teste_primo = True
    if teste_primo:
        print(f'{x}')