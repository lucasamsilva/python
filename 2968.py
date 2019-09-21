import math

entrada = input().split()

valor = float(entrada[0])*float(entrada[1])
string = ""

for i in range(1,9):
    string += str(math.ceil((valor*i*10)/100)) + " "

string += str(math.ceil(valor*0.9))

print(string)