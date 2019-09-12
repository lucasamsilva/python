n = int(input())
texto = "{0}^2 ="
i = 2

while i<=n:
    print(texto.format(i), i**2, end="\n")
    i += 2