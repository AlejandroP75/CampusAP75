def leerInt(msg):
    while True:
        try:
            print("_" * 75)
            iNum = int(input(msg))
            return iNum
        except ValueError:
            print("_" * 75)
            print("Ingrese un numero entero valido")

def leerfloat(msg):
    while True:
        try:
            print("_" * 75)
            while True:
                iNum = float(input(msg))
                if iNum < 0 or iNum > 5:
                    print("Ingrese una nota valida")
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

def notaDefinitiva(nD):
    if nD >= 3.0 and nD <= 5.0:
        return "aprobó"
    return "rebrobó"

estudiantes = {}

while True:
    codigo = leerInt("Ingrese el codigo del esudiante: ")

    if codigo == 999:
        print("\nFIN DEL PROGRAMA")
        break
    print("_" * 75)
    nombre = leerString("Ingrese el nombre del estudiante: ")
    not1 = leerfloat("Ingrese la primer nota: ")
    not2 = leerfloat("Ingrese la segunda nota: ")
    not3 = leerfloat("Ingrese la tercera nota: ")

    estudiantes[codigo] = {}
    estudiantes[codigo]["nombre"] = nombre
    estudiantes[codigo]["not_1"] = not1
    estudiantes[codigo]["not_2"] = not2
    estudiantes[codigo]["not_3"] = not3

    print("\n\n*** INFORME ***")
    print("=" * 30)
    for k in estudiantes.keys():
        nD = (estudiantes[k]["not_1"] * 0.30) + (estudiantes[k]["not_2"] * 0.30) + (estudiantes[k]["not_3"] * 0.40) 
        siNo = notaDefinitiva(nD)
        print(estudiantes[k]["nombre"], f"{siNo} con: {nD}")

    