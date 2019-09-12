aux = input().split()
n = int(aux[0])
m = int(aux[1])
auxpinos = input().split()
pinos = []
soma = 0

for i in range(len(auxpinos)):
    pinos.append(int(auxpinos[i]))

for i in range(len(pinos)-1):
    diferenca = m - (pinos[i])
    pinos[i] = m
    if diferenca != 0:
        pinos[i+1] += diferenca
        soma += (diferenca**2)**(1/2)

print(int(soma))

