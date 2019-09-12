risada = input()
risadavogal = ""

for vogal in risada:
    if vogal == "a" or vogal == "e" or vogal == "i" or vogal == "o" or vogal == "u":
        risadavogal = risadavogal + vogal

vogalinversa = risadavogal
vogalinversa = vogalinversa[::-1]

if risadavogal == vogalinversa:
    print("S")
else:
    print("N")