import json
import os

def clear():
    os.system("clear")

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

def menu():
    while True:
        print("_" * 50)
        print("\nMENU PRINCIPAL PET SHOP ACME\n"
            "\n1.Ver todas las mascotas\n"
            "2.Añadir una nueva mascota\n"
            "3.Mostrar las mascotas por tipo\n"
            "4.Actualizar los datos de una mascota\n"
            "5.Eliminar una mascota de la tienda\n"
            "6.Salir")
        print("_" * 50)
        opc = leerInt("\nIngrese el numero de la opción que desea --> ")
        if opc < 1 or opc > 6:
            print("Ingrese un valor valido")
            continue
        return opc

def cargarDat():
    with open("Campus-main/Repasos/PetShopping.json", "r") as archivo:
        mascotas = json.load(archivo)
    return mascotas

def mosMascotas(dat):
    print("MOSTAR MASCOTAS")
    ind = 1
    for mascotas in dat["pets"]:
        print(f"\nMascota {ind}\n")
        print(f"Tipo:\t{mascotas['tipo']}")
        print(f"Raza:\t{mascotas['raza']}")
        print(f"Talla:\t{mascotas['talla']}")
        print(f"Precio:\t{mascotas['precio']:,.0f}")
        print(f"Servicios:\t")
        for i in mascotas["servicios"]:
            print("\t-", i)    
        ind += 1
    input("\nDigite cualquier tecla para volver al menu principal -->")

def menuTall():
    while True:
        print("\nIngrese la talla de la mascota\n"
            "\n1.Pequeño\n"
            "2.Mediano\n"
            "3.Grande")
        opc = leerInt("\nIngrese el numero de la opción que desea --> ")
        if opc < 1 or opc > 3:
            print("Ingrese un valor valido")
            continue
        return opc

def creMascota(dat):
    print("CREAR MASCOTAS")
    tipMas = leerString("\nIngrese el tipo de la mascota: ")
    razMas = leerString("\nIngrese la raza de la mascota: ")
    opc = menuTall()
    if opc == 1:
        tallMas = "Pequeño"
    elif opc == 2:
        tallMas = "Mediano"
    elif opc == 3:
        tallMas = "Grande"
    preMas = leerInt("\nIngrese el precio de la mascota: ")
    servicios = []
    while True:
        servicios.append(leerString("\nIngrese el servicio: "))
        op = leerString("\n¿Desea ingresar otro servicio? (s/n): ")
        if op.lower() == "s":
            continue
        break
    dat["pets"].append({
        "tipo":tipMas,
        "raza": razMas,
        "talla": tallMas,
        "precio": preMas,
        "servicios": servicios
    })

def subMenu():
    while True:
        print("_" * 50)
        print("\n¿Que tipo de mascota quiere visualizar?\n"
            "\n1.Perro\n"
            "2.Gato\n"
            "3.Chanchito")
        print("_" * 50)
        opc = leerInt("\nIngrese el numero de la opción que desea --> ")
        if opc < 1 or opc > 3:
            print("Ingrese un valor valido")
            continue
        return opc

def mosTipMascotas(dat):
    print("LISTADO DE MASCOTAS SEGUN UN FILTRO")
    op = subMenu()
    if op == 1:
        clear()
        for mascot in dat["pets"]:
            if mascot["tipo"] == "Perro":
                print(f"\nTipo:\t{mascot['tipo']}")
                print(f"Raza:\t{mascot['raza']}")
                print(f"Talla:\t{mascot['talla']}")
                print(f"Precio:\t{mascot['precio']:,.0f}")
                print(f"Servicios:\t")
                for i in mascot["servicios"]:
                    print("\t-", i)    
    elif op == 2:
        clear()
        for mascot in dat["pets"]:
            if mascot["tipo"] == "Gato":
                print(f"Tipo:\t{mascot['tipo']}")
                print(f"Raza:\t{mascot['raza']}")
                print(f"Talla:\t{mascot['talla']}")
                print(f"Precio:\t{mascot['precio']:,.0f}")
                print(f"Servicios:\t")
                for i in mascot["servicios"]:
                    print("\t-", i)   
    else:
        clear()
        for mascot in dat["pets"]:
            if mascot["tipo"] == "Chanchito":
                print(f"Tipo:\t{mascot['tipo']}")
                print(f"Raza:\t{mascot['raza']}")
                print(f"Talla:\t{mascot['talla']}")
                print(f"Precio:\t{mascot['precio']:,.0f}")
                print(f"Servicios:\t")
                for i in mascot["servicios"]:
                    print("\t-", i)   
    input("\nDigite cualquier letra para continuar -->")

def menuAct():
    while True:
        print("\n¿Que desea modificar?\n"
            "\n1.Tipo\n"
            "2.Raza\n"
            "3.Talla\n"
            "4.Precio\n"
            "5.Servicios")
        opc = leerInt("\nIngrese el numero de la opción que desea --> ")
        if opc < 1 or opc > 5:
            print("Ingrese un valor valido")
            continue
        return opc

def actMascotas(dat):
    print("ACTUALIZAR LOS DATOS DE UNA MASCOTA ")
    ind = 1
    for mascotas in dat["pets"]:
        print(f"\nMascota {ind}\n")
        print(f"Tipo:\t{mascotas['tipo']}")
        print(f"Raza:\t{mascotas['raza']}")
        print(f"Precio:\t{mascotas['precio']:,.0f}") 
        ind += 1
    while True:
        opAc = leerInt("\nIngrese el indice de la mascota que desea actualizar: ")
        if opAc < (0) or opAc > (ind - 1):
            print("\nIndice no encontrado, vuelva a intentarlo")
            continue
        break
    op = menuAct()
    if op == 1:
        dat["pets"][opAc-1]["tipo"] = leerString("Ingrese el tipo de la mascota: ")
    elif op == 2:
        dat["pets"][opAc-1]["raza"] = leerString("Ingrese la raza de la mascota: ")
    elif op == 3:
        opc = menuTall()
        if opc == 1:
            dat["pets"][opAc-1]["talla"] ="Pequeño"
        elif opc == 2:
            dat["pets"][opAc-1]["talla"] ="Mediano"
        elif opc == 3:
            dat["pets"][opAc-1]["talla"] ="Grande"
    elif op == 4:
        dat["pets"][opAc-1]["precio"] = leerInt("Ingrese el precio de la mascota: ")
    else:
        dat["pets"][opAc-1]["servicios"] = []
        while True:
            dat["pets"][opAc-1]["servicios"].append(leerString("\nIngrese el servicio: "))
            op = leerString("\n¿Desea ingresar otro servicio? (s/n): ")
            if op.lower() == "s":
                continue
            break
    print("DATOS ACTUALIZADOS")
    input("\nDigite cualquier letra para continuar -->")

def eliMascotas(dat):
    print("ELIMINAR LOS DATOS DE UNA MASCOTA ")
    ind = 1
    for mascotas in dat["pets"]:
        print(f"\nMascota {ind}\n")
        print(f"Tipo:\t{mascotas['tipo']}")
        print(f"Raza:\t{mascotas['raza']}")
        print(f"Precio:\t{mascotas['precio']:,.0f}") 
        ind += 1
    while True:
        opAc = leerInt("\nIngrese el indice de la mascota que desea eliminar ")
        if opAc < (0) or opAc > (ind - 1):
            print("\nIndice no encontrado, vuelva a intentarlo")
            continue
        break
    dat["pets"].pop(opAc-1)
    print("DATOS ELIMINADOS")
    input("\nDigite cualquier letra para continuar -->")

datMascotas = cargarDat()

while True:
    clear()
    op = menu()
    if op == 1:
        clear()
        mosMascotas(datMascotas)
    elif op == 2:
        clear()
        creMascota(datMascotas)
    elif op == 3:
        clear()
        mosTipMascotas(datMascotas)
    elif op == 4:
        clear()
        actMascotas(datMascotas)
    elif op == 5:
        clear()
        eliMascotas(datMascotas)
    else:
        clear()
        print("FIN DEL PROGRAMA")
        break