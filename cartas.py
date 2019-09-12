num = input().split()
seq = []

for i in range (5):
    seq.append(int(num[i]))

cresc = sorted(seq)
decres = sorted(seq, reverse=True)

if seq == cresc:
    print("C")
else:
    if seq == decres:
        print("D")
    else:
        print("N")

