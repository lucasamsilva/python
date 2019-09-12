
lados = input().split()
vetor = []
for i in range(0, 3):
    vetor.append(float(lados[i]))
ordenados = sorted(vetor, reverse=True)
a = float(ordenados[0])
b = float(ordenados[1])
c = float(ordenados[2])

d = True

if a >= b+c:
    print("NAO FORMA TRIANGULO")
    d = False
else:
    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    elif a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    elif a**2 < b**2 + c**2:
        print("TRIANGULO ACUTANGULO")
if d:
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    else:
        if a==b or b==c or c==a:
            print("TRIANGULO ISOSCELES")