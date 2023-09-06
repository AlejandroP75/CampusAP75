segundos = int(input("Ingrese el numero de segundos: "))
horas = segundos // 3600
minutos = (segundos - (3600*horas)) //60
segundos = (segundos - (3600*horas) - (60*minutos))

print("Horas: %d , Minutos: %d , Segundos: %d" % (horas, minutos, segundos))
