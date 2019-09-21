import math

n = int(input())
contador = 0

for p in range(n+1):
    res = (math.factorial(n))/(math.factorial(p)*math.factorial(n-p))
    if (res%2 != 0):
        contador += 1

print(contador)