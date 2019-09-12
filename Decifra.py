crip = input()
alf = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
palavra = []
mensagem = input()

for i in mensagem:
    contador = 0
    for j in crip:
        if i == j:
            palavra.append(alf[contador])
        contador += 1
print(''.join(palavra))