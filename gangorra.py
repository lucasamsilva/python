valores = input().split()

p1 = int(valores[0])
c1 = int(valores[1])
p2 = int(valores[2])
c2 = int(valores[3])

if p1 * c1 == p2 * c2:
    print("0")
if p1 * c1 > p2 * c2:
    print("-1")
if p1 * c1 < p2 * c2:
    print("1")