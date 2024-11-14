def funcao(n):
    x = n.split(",")
    for i in range(len(x)):
        x[i] = int(x[i])
    return print(sum(x))

string = "1,3,4,6,10,76"

funcao(string)