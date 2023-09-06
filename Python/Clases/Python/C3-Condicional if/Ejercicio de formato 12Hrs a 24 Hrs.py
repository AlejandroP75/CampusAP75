iHora = int(input("Ingrese las horas: "))
iMin = int(input("Ingrese los minutos: "))
iSeg = int(input("Ingrese los segundos: "))
sHorario = input("Ingrese AM o PM: ")

if sHorario == "am":
    sHorario = "AM"
elif sHorario == "pm":
    sHorario = "PM"

if sHorario == "PM":
    
    if iHora != 12:
        iHora = iHora + 12
else:
    if iHora == 12:
        iHora = 0

print(f"La hora ingresada en formato de 24 horas seria: {iHora:02d}:{iMin:02d}:{iSeg:02d}") 


