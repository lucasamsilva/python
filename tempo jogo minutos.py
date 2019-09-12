texto = "O JOGO DUROU {0} HORA(S) E {1} MINUTO(S)"

tempos = input().split()
hora_inicio = int(tempos[0])
minuto_inicio = int(tempos[1])
hora_fim = int(tempos[2])
minuto_fim = int(tempos[3])

horas = 0
minutos = 0

horas = hora_fim - hora_inicio

if horas < 0:
    horas = 24 + horas

minutos = minuto_fim - minuto_inicio

if (minutos < 0):
    minutos = 60 + minutos
    horas -= 1
if hora_inicio == hora_fim and minuto_inicio == minuto_fim:
    horas = 24
    minutos = 0
    print(texto.format(horas,minutos))
else:
    print(texto.format(horas, minutos))
