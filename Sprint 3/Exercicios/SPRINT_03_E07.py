a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []

for x in a:
    if x % 2 != 0:
        b.append(x)
print(b)