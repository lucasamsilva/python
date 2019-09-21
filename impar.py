n = input().split()
vetor = []
for num in n:
    vetor.append(int(num))
cont = 0
for num in vetor:
    if num%2 != 0:
        cont += 1

print(cont)