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
        print("\n1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Division")
        print("5. Potencia")
        print("6. Factorial")
        print("7. Salir")
        op = leerInt("\nSeleccione una opción de 1 a 7: ")
        if op < 1 or op > 7:
            msgError("Opcion no valida")
            continue
        return op

def sum():
    print("\n" * 2, "----- 1. SUMAR -----\n")
    iNum1 = leerInt("Ingrese el primer numero: ")
    iNum2 = leerInt("Ingrese el segundo numero: ")
    print("_" * 75)
    print(f"El resultado de la suma es: {iNum1 + iNum2}")
    input("Presione cualquier tecla para volver al menu")

def rest():
    print("\n" * 2, "----- 2. RESTAR -----\n")
    iNum1 = leerInt("Ingrese el primer numero: ")
    iNum2 = leerInt("Ingrese el segundo numero: ")
    print("_" * 75)
    print(f"El resultado de la resta es: {iNum1 - iNum2}")
    input("Presione cualquier tecla para volver al menu")    

def mult():
    print("\n" * 2, "----- 3. MULTIPLICAR -----\n")
    iNum1 = leerInt("Ingrese el primer numero: ")
    iNum2 = leerInt("Ingrese el segundo numero: ")
    print("_" * 75)
    print(f"El resultado de la multiplicacion es: {iNum1 * iNum2}")
    input("Presione cualquier tecla para volver al menu")  

def div():
    print("\n" * 2, "----- 4. DIVIDIR -----\n")
    iNum1 = leerInt("Ingrese el primer numero: ")
    while True:
        iNum2 = leerInt("Ingrese el segundo numero: ")
        if iNum2 == 0:
            print("El segundo numero no puede ser igual a 0")
            continue
        break
    print("_" * 75)
    print(f"El resultado de la división es: {(iNum1 / iNum2):,.1f}")
    input("Presione cualquier tecla para volver al menu")  

def pot():
    print("\n" * 2, "----- 5. POTENCIA -----\n")
    iNum1 = leerInt("Ingrese el primer numero: ")
    iNum2 = leerInt("Ingrese el segundo numero: ")
    print("_" * 75)
    print(f"El resultado del primer numero elevado al segundo es: {iNum1 ** iNum2}")
    input("Presione cualquier tecla para volver al menu")  

def fac():
    print("\n" * 2, "----- 6. FACTORIAL-----\n")
    iNum1 = leerInt("Ingrese un numero: ")
    iFac = 1
    for i in range(1, iNum1 + 1):
        iFac *= i
    print("_" * 75)
    print(f"El resultado del factorial del numero ingresado: {iFac}")
    input("Presione cualquier tecla para volver al menu") 

while True:
    iOpc = menu()

    if iOpc == 1:
        sum()
    elif iOpc == 2:
        rest()
    elif iOpc == 3:
        mult()
    elif iOpc == 4:
        div()
    elif iOpc == 5:
        pot()
    elif iOpc == 6:
        fac()
    elif iOpc == 7:
        print("_" * 75)
        print("\nFin del programa")
        break
    else:
        print("_" * 75)
        msgError("Opcion invalida")              