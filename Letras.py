letra = input()
frase = input()
check = False
contaletra = 0
contapalavra = 1

for espaco in frase:
    if espaco == " ":
        contapalavra = contapalavra + 1;

for let in frase:
    if let == letra and check == False:
        contaletra = contaletra + 1;
        check = True
    if let == " " and check == True:
        check = False

print(round((contaletra/contapalavra)*100,1))
