def checa(vetor):
    for bool in vetor:
        if bool == True:
            return False
    return True

intlamp = input().split()

entrada = input().split()

inicio = []
associações = []
estadoatual=[]

for i in range(int(intlamp[1])):
    inicio.append(False)

for i in range(1,len(entrada)):
    inicio[int(entrada[i])-1] = not inicio[int(entrada[i])-1]

for i in range(int(intlamp[0])):
    associações.append(input().split())

for i in range(int(intlamp[0])):
    del(associações[i][0])

check = True
contador = 0
ativacontador = True
set(inicio)
estadoatual = inicio

while check:
    for i in range(int(intlamp[0])):
        if checa(estadoatual):
            check = False
            break
        else:
            contador += 1
        for valor in associações[i]:
            estadoatual[int(valor)-1] = not estadoatual[int(valor)-1] #TRECHO DO CÓDIGO ONDE O VETOR INICIO É MODIFICADO
    if estadoatual == inicio and contador%int(intlamp[0]) == 0:
      check = False
      print("-1")
      ativacontador = False
      break

if ativacontador:
    print(contador)