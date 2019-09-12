while True:
  try:
    dados = input().split()
    v = int(dados[0])
    t= int(dados[1])
    print(v*(t*2))
  except EOFError:
    break