iDia = int(input("Ingrese el día: "))
iMes = int(input("Ingrese el mes: "))
iAn = int(input("Ingrese el año: "))

sBis = ""

if iAn % 4 == 0:
    sBis = "sí"
    if iAn % 100 == 0 and iAn % 400 != 0:
        sBis = "no"
else:
    sBis = "no"

if iDia == 31 and iMes == 12:
    iAn = iAn + 1 

if sBis == "sí":
    if iMes == 1 or iMes == 3 or iMes == 5 or iMes == 7 or iMes == 8 or iMes == 10 or iMes == 12:
        if iDia == 31:
            iDia = 1
            iMes = iMes + 1
        else:
            iDia = iDia + 1
            iMes = iMes + 1
    elif iMes == 4 or iMes == 6 or iMes == 9 or iMes == 11:
        if iDia == 30:
            iDia = 1
            iMes = iMes + 1
        else:
            iDia = iDia + 1
            iMes = iMes + 1
    else:
        if iDia == 29:
            iDia = 1
            iMes = iMes + 1
        else:
            iDia = iDia + 1
            iMes = iMes + 1
else:
    if iMes == 1 or iMes == 3 or iMes == 5 or iMes == 7 or iMes == 8 or iMes == 10 or iMes == 12:
        if iDia == 31:
            iDia = 1
            iMes = iMes + 1
        else:
            iDia = iDia + 1
    elif iMes == 4 or iMes == 6 or iMes == 9 or iMes == 11:
        if iDia == 30:
            iDia = 1
            iMes = iMes + 1
        else:
            iDia = iDia + 1
    else:
        if iDia == 28:
            iDia = 1
            iMes = iMes + 1
        else:
            iDia = iDia + 1  

if iMes == 13:
    iMes = 1 

print(f"La fecha del dia siguiente es: {iDia:02d}/{iMes:02d}/{iAn:04d}")