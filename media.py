x = []
soma = 0

x.append(int(input("Digite a primeira nota: ")))
x.append(int(input("Digite a segunda nota: ")))
x.append(int(input("Digite a terceira nota: ")))
x.append(int(input("Digite a quarta nota: ")))

for i in range (0,4):
    soma += x[i]

print("A média aritmética é", soma/4.0)