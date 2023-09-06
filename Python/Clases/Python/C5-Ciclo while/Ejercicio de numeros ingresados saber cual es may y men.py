iNum = 1
iMen = float("Inf")
iMay = 0

while (iNum > 0 ):
    iNum = int(input("Ingrese un numero: "))
    if iNum < 0:
        break

    if iNum < iMen:
        iMen = iNum
    if iNum > iMay:
        iMay = iNum
    
print(f"De los datos ingresados el numero mayor es: {iMay}")
print(f"de los datos ingresados el numero menor es: {iMen}")
