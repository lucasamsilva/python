texto = "{0} dias, {1} horas, {2} minutos e {3} segundos."

entrada = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = entrada//86400
horas = (entrada % 86400)//3600
minutos = ((entrada % 86400) % 3600)//60
segundos = ((entrada % 86400) % 3600) % 60
print(texto.format(dias,horas,minutos,segundos))