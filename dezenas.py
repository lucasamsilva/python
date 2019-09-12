valor = input("Digite um número inteiro: ")

if(len(valor)>1):
    print("O dígito das dezenas é", valor[len(valor) - 2])
else:
    print("O dígito das dezenas é 0")