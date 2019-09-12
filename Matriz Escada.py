def localizaposicao(vetor):
    for i in range(len(vetor)):
        conv = int(vetor[i])
        if conv > 0:
            return i
    return len(vetor) + 1

aux = input().split()
n = int(aux[0])
m = int(aux[1])
check = False
linhaatual = input().split()
ultimapos =  localizaposicao(linhaatual)

for i in range(n-1):
    aux = input().split()
    posicao = localizaposicao(aux)
    if posicao > ultimapos or (ultimapos == posicao and aux[ultimapos] == 0):
        ultimapos = posicao
    else:
        print("\nN")
        check = True
        break
if not check:
    print("S")
