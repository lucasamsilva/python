tam = int(input())
linhas = []
sai = 0
frase = ""
for i in range(tam):
    linhas.append(input())

for i in range(tam):
    frase += linhas[i]


for i in range(tam,((tam*tam)-tam)):
    if i % tam == 0 and frase[i]=="<":
        sai += 1
    if (i % tam) == (tam-1) and frase[i] == ">":
        sai += 1

for i in range(0,tam-1):
    if i == 0:
        if frase[i] == "<" or frase[i] == "A":
            sai += 1
    if i == tam - 1:
        if frase[i] == ">" or frase[i] == "A":
            sai += 1

for i in range((tam*tam)-tam,tam*tam):
    if i % tam == 0:
        if frase[i] == "<" or frase[i] == "V":
            sai += 1
    if i % tam == tam -1:
        if frase[i] == ">" or frase[i] == "V":
            sai += 1

print(tam*tam-sai)