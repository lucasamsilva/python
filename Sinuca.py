inicio = int(input())
aux = input().split()
posicao = []
arm = []

for i in aux:
    posicao.append(int(i))
    arm.append(0)

while inicio>1:
    for i in range(len(posicao)-1):
        arm[i] = (posicao[i]*posicao[i+1])
    posicao = arm
    inicio -= 1

if (posicao[0] > 0):
    print("preta")
else:
    print("branca")