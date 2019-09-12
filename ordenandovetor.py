import random

vetor = []
for x in range(0,100):
    vetor.append(random.randint(0,1000))
print(vetor)
vetor.sort()
print(vetor)