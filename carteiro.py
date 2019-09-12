def busca_binaria(v, p, r,x):
    #parâmetros = (vetor, posicao inicial, posicaofinal, valor a ser encontrado)
    #se posicao inicial <= posicao final então o vetor ainda não foi totalmente percorrido
    if p <= r:
        q = (p+r) // 2 #encontra o meio do vetor
        if x > v[q]: #se o valor do meio for menor que o valor a ser encontrado
            return busca_binaria(v, q+1, r,x) #Chama a função recursivamente passando como início o meio do vetor
        elif x < v[q]: #se o valor do meio for maior que o valor a ser encontrado
            return busca_binaria(v, p, q-1,x)  #chama a função recursivamente passando como fim o meio do vetor
        else:
            return q #quando o valor é encontrado retorna sua posição no vetor
    return -1 #se o valor não é encontrado retorna-se -1


soma = 0
aux = 0

tamanhos = input().split()

n = int(tamanhos[0])
m = int(tamanhos[1])
ncasas = []
nencomenda = []
posicaoatual = 0

valor = input().split()
for i in range (n):
    ncasas.append(int(valor[i]))
valor = input().split()
for i in range(m):
    nencomenda.append(int(valor[i]))

for i in range(len(nencomenda)): #percorre o vetor das encomendas
        posicaoencomenda = busca_binaria(ncasas, 0, len(ncasas), nencomenda[i]) #posicaoencomenda recebe a posicao onde está a casa que a encomenda tem q ser entregue
        if posicaoatual != posicaoencomenda: #se a posicaoatual não é igual a posicaoencomenda então devemos calcular qual a distancia até a casa onde devemos entregar
            soma = soma + (((posicaoencomenda - posicaoatual)**2)**(1/2)) #calcula o deslocamento até a casa
            posicaoatual = posicaoencomenda #guarda a ultima casa visitada

print(int(soma))