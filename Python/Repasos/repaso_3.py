import os

def poblarIniciales(empleados):
    empleados.append({
        "documento": 1,
        "nombre": "Howard",
        "edad": 25,
        "eps": "Sura"
    })

    empleados.append({
        "documento": 2,
        "nombre": "Nahomi",
        "edad": 33,
        "eps": "Solsalud"
    })
    empleados.append({
        "documento": 3,
        "nombre": "Sarita",
        "edad": 21,
        "eps": "SinergiaSalud"
    })
    empleados.append({
        "documento": 4,
        "nombre": "Juliana",
        "edad": 17,
        "eps": "La EPS de SUBIDA"
    })

def validarInput(mensaje):
    data = input(mensaje)
    while(data.strip() == ''):
        print("\nIngrese algún dato\n")
        data = input(mensaje)
    return data

def validaDocumento(id, empleados):
    for i in range(len (empleados)):
        if (empleados[i]['documento'] == id):
            return True
    return False

def ingresarDatos():
    os.system('clear')

    documento = validarInput("Digite el Documento: ")
    while(validaDocumento(documento,empleados)):
        print("\nEl documento ya existe\n")
        documento = validarInput("Digite el Documento: ")
        
    nombre = validarInput("Digite el Nombre: ")
    edad = validarInput("Digite el Edad: ")
    eps = validarInput("Digite el EPS: ")

    empleados.append({
        "documento": documento,
        "nombre": nombre,
        "edad": edad,
        "eps": eps
    })

def eliminarRegistro():
    os.system('clear')
    doc = int(input('Ingrese el documento que desea eliminar'))
    for i in range(len(empleados)):
        if(empleados[i]['documento'] == doc):
            print("_" * 50)
            print(f"Empleado eliminado\n")
            print("Documento: ", empleados[i]["documento"])
            print("Nombre: ", empleados[i]["nombre"])
            print("Edad: ", empleados[i]["edad"])
            print("EPS: ", empleados[i]["eps"])
            print("_" * 50)
            input("Digite cualquier tecla para continuar-->")
            empleados.pop(i)
            return

    return print('\nNo existe el registro con ese documento\n')

def reportarListado():
    os.system('clear')
    for i in range(len(empleados)):
        print("_" * 50)
        print(f"Empleado {i+1}\n")
        print("Documento: ", empleados[i]["documento"])
        print("Nombre: ", empleados[i]["nombre"])
        print("Edad: ", empleados[i]["edad"])
        print("EPS: ", empleados[i]["eps"])
    print("_" * 50)
    input("Digite cualquier tecla para continuar-->")

def buscarRegistro():
    os.system('clear')
    doc = int(input('Ingrese el documento que desea buscar'))
    for i in range(len(empleados)):
        if(empleados[i]['documento'] == doc):
            print("_" * 50)
            print("Documento: ", empleados[i]["documento"])
            print("Nombre: ", empleados[i]["nombre"])
            print("Edad: ", empleados[i]["edad"])
            print("EPS: ", empleados[i]["eps"])
            print("_" * 50)
            input("Digite cualquier tecla para continuar-->")
            return

def actualizarRegistro():
    os.system('clear')
    doc = int(input('Ingrese el documento del empleado que desea actualizar'))
    for i in range(len(empleados)):
        if(empleados[i]['documento'] == doc):
            print("\nSelecciona la opción de lo que desea eliminar")
            print(" "*6 + "1) Nombre")
            print(" "*6 + "2) Edad")
            print(" "*6 + "3) EPS")  #****
            print()

            opcion = int(input('opcion -> '))

            if(opcion < 1 or opcion > 3):
                return print('\nEl número debe ser entre 0 y 3\n')
            
            if opcion == 1:
                nombre = validarInput("Digite el nuevo Nombre: ")
                empleados[i]["nombre"] = nombre
            elif opcion == 2:
                edad = validarInput("Digite la nueva Edad: ")
                empleados[i]["edad"] = edad
            else:
                eps = validarInput("Digite la nueva EPS: ")
                empleados[i]["eps"] = eps
            print("Registro actualizado")
            return

def menu():
    seguir = True
    while seguir:
        print("\nSelecciona la opción que desee")
        print(" "*6 + "1) Ingresar un nuevo registro")
        print(" "*6 + "2) Eliminar un registro")
        print(" "*6 + "3) Mostrar listado total")
        print(" "*6 + "4) Buscar y mostrar un registro")  #****
        print(" "*6 + "5) Actualizar un registro")  #****
        print(" "*6 + "6) Salir del Programa\n")  #****
        print()

        opcion = int(input('opcion -> '))

        if(opcion == 6):
            seguir = False
            return print('\nFin del programa\n')

        if(opcion < 1 or opcion > 6):
            return print('\nEl número debe ser entre 0 y 6\n')

        switch = { 1: ingresarDatos, 2: eliminarRegistro, 3: reportarListado, 4:buscarRegistro, 5:actualizarRegistro }

        switch[opcion]()
empleados = []
poblarIniciales(empleados)
menu()