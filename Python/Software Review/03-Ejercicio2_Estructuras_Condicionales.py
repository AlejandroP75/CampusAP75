iAn = int(input("Ingrese el año para saber si es bisiesto o no: "))
sBis = ""

if iAn % 4 == 0:
    sBis = "sí"
    if iAn % 100 == 0 and iAn % 400 != 0:
        sBis = "no"
else:
    sBis = "no"

print(f"El año {iAn} {sBis} es bisiesto")