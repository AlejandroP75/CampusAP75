iHorasEntrada = int(input("Ingrese el numero de horas: "))
iMinutosEntrada = int(input("Ingrese el numero de minutos: "))
iMinutosExtra = int(input("Ingrese el numero de minutos que quiere adicionar: "))

iHorasMinutos = iHorasEntrada * 60
iNuevosMinutos = iHorasMinutos + iMinutosEntrada + iMinutosExtra
print(iNuevosMinutos)
iHorasSalida = iNuevosMinutos / 60
iMinutosSalida = iNuevosMinutos % 60

print(f"Hora: {iHorasEntrada}:{iMinutosEntrada}\n"
      f"Minutos: {iMinutosExtra}\n"
      f"Nueva Hora: {int(iHorasSalida)}:{iMinutosSalida:02d}")