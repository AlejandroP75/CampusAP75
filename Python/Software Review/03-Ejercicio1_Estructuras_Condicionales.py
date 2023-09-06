iNum1 = int(input("Ingrese el primer numero entero: "))
iNum2 = int(input("Ingrese el segundo numero entero: "))
iNum3 = int(input("Ingrese el tercer numero entero: "))

iMay = 0
iMed = 0
iMen = 0

if iNum1 > iNum2 and iNum1 > iNum3:
    if iNum1 > iNum3:
        iMay = iNum1
        if iNum2 > iNum3:
            iMed = iNum2
            iMen = iNum3
        else:
            iMed = iNum3
            iMen = iNum2
elif iNum2 > iNum1 and iNum2 > iNum3:
    iMay = iNum2
    if iNum1 > iNum3:
            iMed = iNum1
            iMen = iNum3
    else:
            iMed = iNum3
            iMen = iNum1
else:
    iMay = iNum3
    if iNum2 > iNum1:
            iMed = iNum2
            iMen = iNum1
    else:
            iMed = iNum1
            iMen = iNum2

print(f"Numero mayor: {iMay}\n"
      f"Numero del medio: {iMed}\n"
      f"Numero menor: {iMen}")