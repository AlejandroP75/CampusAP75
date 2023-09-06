iNum = 1

while (iNum > 0 ):
    iNum = int(input("Ingrese un numero: "))
    prim = "sí"
    for i in range(2, iNum):
        if iNum % i == 0:
            prim = "no"
    if iNum > 0:
        if prim != "no":
            print(f"El numero {iNum} es primo")
        else:
            print(f"El numero {iNum} no es primo")
