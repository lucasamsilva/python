n = int(input())
dentro = 0
fora = 0

for i in range (0,n):
    numeros = int(input())
    if 21 > numeros > 9:
        dentro += 1
    else:
        fora += 1
print(dentro, "in")
print(fora, "out")

