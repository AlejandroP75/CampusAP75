def leerInt(msg):
    while True:
        try:
            print("_" * 75)
            iNum = int(input(msg))
            while True:
                if iNum < 1 or iNum > 5:
                    print("Por favor ingrese un numero de 1 a 5")
                    continue
                break
            return iNum
        except ValueError:
            print("_" * 75)
            print("Ingrese un numero entero valido")

def leerString(msg):
    while True:
        try:
            sNom = input(msg)
            if sNom.strip() == "":
                print("\nPor favor ingrese un nombre valido")
                continue
            return sNom
        except Exception as e:
            print("\nError al ingresar un nombre" , e.message)

def servEner(sNomb, iEstr):
    if iEstr == 1:
        print(f"\n{sNomb} su tarifa basica del servicio de energia es: $10.000")
    elif iEstr == 2:
        print(f"\n{sNomb} su tarifa basica del servicio de energia es: $15.000")
    elif iEstr == 3:
        print(f"\n{sNomb} su tarifa basica del servicio de energia es: $30.000")
    elif iEstr == 4:
        print(f"\n{sNomb} su tarifa basica del servicio de energia es: $50.000")
    elif iEstr == 5:
        print(f"\n{sNomb} su tarifa basica del servicio de energia es: $65.000")

print("_" * 70)
sNom = leerString("\nIngrese el nombre: ")
iEst = leerInt("\nIngrese el numero del estrato: ")
print("_" * 70)
servEner(sNom, iEst)
print("\nFIN DEL PROGRAMA")