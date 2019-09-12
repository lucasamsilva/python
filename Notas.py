numalunos = int(input())
notas = input().split()
notasinteiras = []
maiorqntd = 0
maiornota = 0
notaatual = -1
for i in range(len(notas)):
    notasinteiras.append(int(notas[i]))

notasinteiras.sort()

for i in range(len(notasinteiras)):
    if notasinteiras[i] != notaatual:
        qntd = notasinteiras.count(notasinteiras[i])
        if qntd >= maiorqntd:
            maiorqntd = qntd
            maiornota = notasinteiras[i]
notaatual = notasinteiras[i]
print(maiornota)