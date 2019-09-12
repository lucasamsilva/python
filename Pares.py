x = 0
for i in range (0, 5):
    n = int(input())
    if n%2 == 0:
        x += 1
texto = "{0} valores pares"
print(texto.format(x))
