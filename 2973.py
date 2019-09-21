import math

ent1 = input().split()
ent2 = input().split()

n = int(ent1[0])
c = int(ent1[1])
t = int(ent1[2])

sacos = []

for j in ent2:
    sacos.append(int(j))
inicio = 0
fim = math.ceil(n/c)
maior = -1

for i in range(1,n%c):
    inicio = 0
    fim = i
    while fim <= n:
        valor = math.ceil((sum(sacos[inicio:fim])) / t)
        if valor > maior:
            maior = valor
        inicio += i
        fim += i
    if maior < melhorres:
        melhorres = maior
        print(melhorres)

print(maior)