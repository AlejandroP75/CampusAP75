import json

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

def cargarInfo(ruta, datos):
    aJ = open(ruta, "a+", encoding = "utf-8")
    aJ.seek(0)
    try:
        datos = json.load(aJ)
    except Exception as e:
        datos = {}
    aJ.close()
    return datos

def menu():
    while True:
        print("_" * 50)
        print("\nMENU PRINCIPAL\n"
            "\n1.Estudiantes\n"
            "2.Notas\n"
            "3.Reportes\n"
            "4.Salir")
        print("_" * 50)
        opc = leerInt("\nIngrese el numero de la opción que desea --> ")
        if opc < 1 or opc > 4:
            print("Ingrese un valor valido")
            continue
        return opc

def menuEst():
    while True:
        print("_" * 50)
        print("\nMenu estudiantes\n"
            "\n1.Agregar\n"
            "2.Modificar\n"
            "3.Buscar\n"
            "4.Eliminar\n"
            "5.Salir")
        print("_" * 50)
        opc = leerInt("\nIngrese el numero de la opción que desea --> ")
        if opc < 1 or opc > 5:
            print("Ingrese un valor valido")
            continue
        return opc

def funAgreEst(ruta, datos): 
    while True:
        gra = leerString("Ingrese el grado del estudiante: ")
        id = leerInt("Ingrese el id del estudiante: ")
        nom = leerString("Ingresar el nombre del estudiante: ")
        while True:
            gen = leerString("Ingrese el genero del estudiante (F o M): ")
            genMa = gen.upper()
            if genMa != "F" and genMa != "M":
                print("Ingrese F para femenino o M para masculino")
                continue
            break
        if datos == {}:
            datos[gra] = {}
        if gra in datos:
            pass
        else:
            datos[gra] = {}
        datos[gra][id] = {}
        datos[gra][id]["Nombre"] = nom
        datos[gra][id]["Genero"] = genMa
        with open(ruta, "w") as archivo:
            json.dump(datos, archivo)
            print("Se ha añadido al estudiante")
        op = leerInt("¿Desea ingresar a otro estudiante? (1 es sí y 2 es no)")
        if op == 1:
            continue
        break
        
def funModEst(ruta, datos):
    while True:
        while True:
            gra = leerString("Ingrese el grado del estudiante: ")
            if gra in datos:
                break
            else:
                print("El grado al que intenta acceder no esta registrado")
                continue
        while True:
            id = leerInt("Ingrese el id del estudiante: ")
            if str(id) in datos[gra]:
                break
            else:
                print("El estudiante al que intenta acceder no esta registrado")
        print("¿Que desea nodificar?")
        print("\n1.Nombre")
        print("2.Genero")
        while True:
            op = leerInt("\nIngrese el numero de la opción que desea -->")
            if op < 1 or op > 2:
                print("Ingrese una opción valida")
                continue
            break
        if op == 1:
            nueNom = leerString("Ingrese el nuevo nombre del estudiante: ")
            datos[gra][str(id)]["Nombre"] = nueNom
        elif op == 2:
            nueGen = leerString("Ingrese el nuevo genero del estudiante: ")
            datos[gra][str(id)]["Genero"] = nueGen.upper()
        with open(ruta, "w") as archivo:
            json.dump(datos, archivo)
            print("Se ha modificado al estudiante")
        op = leerInt("¿Desea modificar a otro estudiante? (1 es sí y 2 es no)")
        if op == 1:
            continue
        break

def funBusEst(datos):
    while True:
        while True:
            gra = leerString("Ingrese el grado del estudiante: ")
            if gra in datos:
                break
            else:
                print("El grado al que intenta acceder no esta registrado")
                continue
        while True:
            id = leerInt("Ingrese el id del estudiante: ")
            if str(id) in datos[gra]:
                break
            else:
                print("El estudiante al que intenta acceder no esta registrado")
        print(f"Estudiante: {datos[gra][str(id)]['Nombre']}"
            f"\nID: {id}"
            f"\nGrado: {gra}"
            f"\nGenero: {datos[gra][str(id)]['Genero']}")
        op = leerInt("¿Desea buscar a otro estudiante? (1 es sí y 2 es no)")
        if op == 1:
            continue
        break

def funElimEst(ruta, datos):
    while True:
        while True:
            gra = leerString("Ingrese el grado del estudiante: ")
            if gra in datos:
                break
            else:
                print("El grado al que intenta acceder no esta registrado")
                continue
        while True:
            id = leerInt("Ingrese el id del estudiante: ")
            if str(id) in datos[gra]:
                break
            else:
                print("El estudiante al que intenta acceder no existe")
        datos[gra].pop(str(id))
        with open(ruta, "w") as archivo:
            json.dump(datos, archivo)
            print("Se ha eliminado al estudiante")
        op = leerInt("¿Desea eliminar a otro estudiante? (1 es sí y 2 es no)")
        if op == 1:
            continue
        break

def funEst(ruta, datos):
    while True:
        op = menuEst()
        if op == 1:
            funAgreEst(ruta, datos)
            input("\nPresione cualquier tecla para volver al menu de estudiantes --> ")
        elif op == 2:
            funModEst(ruta, datos)
            input("\nPresione cualquier tecla para volver al menu de estudiantes --> ")
        elif op == 3:
            funBusEst(datos)
            input("\nPresione cualquier tecla para volver al menu de estudiantes --> ")
        elif op == 4:
            funElimEst(ruta, datos)
            input("\nPresione cualquier tecla para volver al menu de estudiantes --> ")
        else:
            input("\nPresione cualquier tecla para volver al menu principal --> ")
            break

def funNot(ruta, datos):
    lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while True:
        gra = leerString("Ingrese el grado del estudiante: ")
        if gra in datos:
            break
        else:
            print("El grado al que intenta acceder no esta registrado")
            continue
    # for i in range(5):
    #     for e in datos[gra].keys():
    #         lista[i] = datos[gra][e]["Nombre"]
    # print(lista)
    
    for e in datos[gra].keys():
        lista = [datos[gra][e]["Nombre"], datos[gra][e]["Genero"]]
        print(f"Grado: {gra}\tEstudiante: {lista[0]}\tId: {e}\tGenero:{lista[1]}")
        entNotas = input(f"Ingrese las notas del estudiante separado por espacio:")
        lstNotas = entNotas.split(" ")
        datos[gra][e]["Notas"] = lstNotas
    
    with open(ruta, "w") as archivo:
        json.dump(datos, archivo)
        print("Se han añadido las notas de cada estudiante")

def funRep(ruta):
    pass

ruta = "Campus-main\Simulacros\Python\Instituto ACME\InstitutoACME.json"
datos = {}
while True:
    datosCar = cargarInfo(ruta, datos)
    op = menu()
    if op == 1:
        funEst(ruta, datosCar)
    elif op == 2:
        funNot(ruta, datosCar)
        input("\nPresione cualquier tecla para continuar al menu principal --> ")
    elif op == 3:
        funRep(ruta, datosCar)
        input("\nPresione cualquier tecla para continuar al menu principal --> ")
    else:
        print("Fin del programa de gestión del instituto ACME")
        input("Presione cualquier tecla para salir --> ")
        break