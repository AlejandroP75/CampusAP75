import os

def clear():
    os.system('clear')

def leerInt(msg):
    while True:
        try:
            iNum = int(input(msg))
            return iNum
        except ValueError:
            print("_" * 75)
            print("Ingrese un numero entero valido")

def leerFloat(msg):
    while True:
        try:    
            while True:
                iNum = float(input(msg))
                if iNum < 0 or iNum > 5:
                    print("\nLa nota tiene que estar en el rango permitido (0.0 - 5.0), vuelva a ingresar la nota")
                    continue
                break
            return iNum
        except ValueError:
            print("_" * 75)
            print("Ingrese un numero valido")

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

def menu():
    while True:
        print("_" * 50)
        print("\nMENU PRINCIPAL \n"
            "\n1.Agregar estudiante\n"
            "2.Buscar estudiante\n"
            "3.Actualizar estudiante\n"
            "4.Eliminar estudiante\n"
            "5.Calcular nota estudiante\n"
            "6.Lista de estudiantes y promedio del curso")
        print("_" * 50)
        opc = leerInt("\nIngrese el numero de la opción que desea --> ")
        if opc < 1 or opc > 6:
            print("Ingrese un valor valido")
            continue
        return opc

def agreEst(estudiantes):
    while True:
        codEst = leerInt("\nIngrese el codigo del estudiante: ")
        nomEst = leerString("\nIngrese el nombre completo del estudiante: ")
        not1 = leerFloat("\nIngrese la primera nota parcial: ")
        not2 = leerFloat("\nIngrese la segunda nota parcial: ")
        not3 = leerFloat("\nIngrese la tercera nota parcial: ")
        estudiantes[codEst] = {}
        estudiantes[codEst] = {
            "Nombre":nomEst,
            "Notas":[not1, not2, not3]
            }
        print("\nEstudiante registrado")
        opc = leerString("\nDigite la letra s si desea agregar a otro estudiante: ")
        if opc.lower() == "s":
            continue
        break

def busEst():
    est = leerInt("\nIngrese el codigo del estudiante que desea buscar: ")
    if est in estudiantes.keys():
        print("\nEstudiante encontrado")
        print("\nCodigo: ", est)

def actEst():
    pass

def eliEst():
    pass

def calNot():
    pass

def lisEst():
    pass

estudiantes = {}
print(estudiantes)
while True:
    print(estudiantes.keys())
    op = menu()
    if op == 1:
        agreEst(estudiantes)
    elif op == 2:
        busEst()
    elif op == 3:
        actEst()
    elif op == 4:
        eliEst()
    elif op == 5:
        calNot()
    elif op == 6:
        lisEst()
    else:
        input("FIN DEL PROGRAMA")
