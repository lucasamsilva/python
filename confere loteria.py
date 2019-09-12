resultado = []
numeros = []
acertos = 0

for i in range(15):
    resultado.append(int(input()))

while True:
    for i in range(15):
        numeros.append(int(input()))
        if numeros[i] == 0:
            break

    for i in resultado:
        for j in numeros:
            if i == j:
                acertos += 1


print("Resultado:", acertos)