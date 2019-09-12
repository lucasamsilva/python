d = 1
n = 1

valores = input().split()
d = valores[0]
n = valores[1]
while d!="0" and n!="0":
    n = n.replace(d,"")
    if n == "":
        print("0")
    else:
        print(int(n), end="\n")
    valores = input().split()
    d = valores[0]
    n = valores[1]