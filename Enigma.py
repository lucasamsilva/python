mensagem = input()
crib = input()
pos = 0

for letra in range(len(mensagem)-len(crib) + 1):
    pos += 1
    for j in range(len(crib)):
        if crib[j] == mensagem[letra+j]:
            pos -= 1
            break

print(pos)

