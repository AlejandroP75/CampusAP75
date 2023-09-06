def leerInt(msg):
    while True:
        try:
            print("_" * 75)
            iNum = int(input(msg))
            return iNum
        except ValueError:
            print("_" * 75)
            print("Ingrese un numero entero valido")

def msgError(msg):
    print("ERROR.", msg)

def menu():
    while True:
        print("_" * 75)
        print("\nMENU")
        print("_" * 75)
        print("\n1. Cantidad de palabras en un String")
        print("2. Calcular el mcd de dos números")
        print("3. Calcular el IVA de una factura")
        print("4. Salir")
        op = leerInt("\nSeleccione una opción de 1 a 4: ")
        if op < 1 or op > 4:
            msgError("Opcion no valida")
            continue
        return op

def palabrasString():
    print("_" * 75)
    print("\n----- 1. CANTIDAD DE PALABRAS EN UN STRING -----")
    sString = input("Ingrese el string: ")
    print("_" * 75)
    iCont = 0
    for i in range(0, len(sString)):
        if sString[i] == " ":
            iCont += 1
    print(f"El string ({sString}) contiene {iCont + 1} palabras")
    input("\nPresione cualquier tecla para volver al menu--->")
    pass

def metEuclides(iNum1, iNum2):
    fModDiv = iNum1 % iNum2
    if fModDiv == 0:
        print(f"El mcd de {iNum1} y {iNum2} es {iNum2}")
    else:
        while True:
            fModDivn = iNum2 % fModDiv
            if fModDivn == 0:
                print(f"\nEl mcd de los numeros ingresados es {fModDiv}")
                break
            iNum2 = fModDiv
            fModDiv = fModDivn
            continue

def mcd():
    print("_" * 75)
    print("\n----- 2. CALCULAR EL MCD DE DOS NUMEROS -----")
    iNum1 = leerInt("\nIngrese el primer numero: ")
    iNum2 = leerInt("\nIngrese el segundo numero: ")
    print("_" * 75)
    if iNum1 >= iNum2:
        metEuclides(iNum1, iNum2)
        
    else:
        metEuclides(iNum2, iNum1)

    input("\nPresione cualquier tecla para volver al menu--->")    

def iva(iValProduc, iIva = 21):
    print("_" * 75)
    print("\n----- 3. CALCULAR EL IVA DE UNA FACTURA -----")
    iProducIva = iValProduc + (iValProduc * (iIva / 100))
    print("_" * 75)
    print("\nFACTURA\n"
          f"\nValor del producto: {iValProduc:,.0f}\n"
          f"Porcentaje de IVA: {iIva}%\n"
          f"Total a pagar: {iProducIva:,.0f}")
    input("\nPresione cualquier tecla para volver al menu--->")  

while True:
    iOpc = menu()

    if iOpc == 1:
        palabrasString()
    elif iOpc == 2:
        mcd()
    elif iOpc == 3:
        while True:
            iValProducto = leerInt("\nIngrese el valor del producto: ")
            if iValProducto <= 0:
                print("\nEl valor del prodcuto tiene que ser mayor que 0")
                continue
            break
        while True:
            iPorIva = leerInt("\nIngrese el porcentaje de IVA que quiere aplicar, si desea aplicar el IVA predetermiando digite 0: ")
            if iPorIva < 0:
                print("\nEl porcentaje del IVA no puede ser negativo")
                continue
            break
        if iPorIva == 0:
            iva(iValProducto)
        else:
            iva(iValProducto, iPorIva)
    elif iOpc == 4:
        print("_" * 75)
        print("\nFin del programa")
        break
    else:
        print("_" * 75)
        msgError("Opcion invalida")              