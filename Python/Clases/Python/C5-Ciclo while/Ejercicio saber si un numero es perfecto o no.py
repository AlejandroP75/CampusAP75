iN1 = int(input("Ingrese el numero para saber si es perfecto o no: "))
iCont = 1
iNum = 0

while iCont != iN1:
    if (iN1 % iCont) == 0:
        iNum = iNum + iCont
    iCont = iCont + 1
    
print("-" * 50)
if iNum == iN1:
    print(f"El numero {iN1} es perfecto")
else:
    print(f"El numero {iN1} no es perfecto")