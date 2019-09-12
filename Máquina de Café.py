a1 = int(input())
a2 = int(input())
a3 = int(input())

r1 = (a2*2+a3*4)
r2 = (a3*2+a1*2)
r3 = (a1*4 + a2*2)

if r1 <= r2 and r1 <= r3:
    print(r1)
elif r2 <= r1 and r2 <= r3:
    print(r2)
else:
    print(r3)