n = int(input())
i = 0
while i<=6:
    if n % 2 != 0:
        print(n)
        n += 2
    else:
        n += 1
    i += 1