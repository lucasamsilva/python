valores = input().split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

if (a == b or b == c or a == c or a == b + c or b == a + c or c == a + b):
    print("S")
else:
    print("N")