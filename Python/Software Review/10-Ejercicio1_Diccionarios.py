def leerInt(msg):
    while True:
        try:
            iNum = int(input(msg))
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
        print("_" * 75)
        print("MENU")
        print("\n1. Agregar empleado")
        print("2. Modificar empleado")
        print("3. Buscar empleado")
        print("4. Eliminar empleado")
        print("5. Lista empleados")
        print("6. Listar nomina de un empleado")
        print("7. Listar nomina de todos los empleados")
        print("8. Salir")
        opc = leerInt("\nSeleccione una opción de 1 a 8: ")
        if opc < 1 or opc > 8:
            print("Ingrese una opción valida")
            continue
        return opc

def agregar(empleados, ids, nom, horasT, valorH):
    empleados[ids] = {}
    empleados[ids]["nombre"] = nom
    empleados[ids]["HorasT"] = horasT
    empleados[ids]["ValorH"] = valorH
    print(empleados)
    
def modificar(empleados):
    id = leerInt("\nIngrese el id del empleado: ")
    for k in empleados.keys():
        if k == id:
            e = k
            break

    print("_"*75)
    print("MENU DE MODIFICACION")
    print("\n1. Nombre")
    print("2. Horas trabajadas")
    print("3. Valor de la hora")
    while True:
        op = leerInt("\nSeleccione el que quiere modificar: ")
        if op < 1 or op > 3:
            print("Ingrese un valor valido")
            continue
        break
    if op == 1:
        print("_" * 75)
        print("Modificar nombre")
        nueNom = leerString("Ingrese el nuevo nombre: ")
        empleados[e]["nombre"] = nueNom
    elif op == 2:
        print("_" * 75)
        print("Modificar horas trabajadas")
        while True:
            nueHor = leerInt("Ingrese el nuevo numero de horas trabajadas del empleado: ")
            if nueHor < 1 or nueHor > 160:
                print("El numero de horas tiene que estar entre 1 y 160")
                continue
            break
        empleados[e]["HorasT"] = nueHor
    elif op == 3:
        print("_" * 75)
        print("Modificar valor de la hora")
        while True:
            nueValor = leerInt("Ingrese el valor unitario de la hora: ")
            if nueValor < 8000 or nueValor > 150000:
                print("El nuevo valor de la horas tiene que estar entre 8.000 y 150.000")
                continue
            break    
        empleados[e]["ValorH"] = nueValor          

def buscar(empleados): 
    id = leerInt("\nIngrese el id del empleado: ")
    for k in empleados.keys():
        if k == id:
            e = k
            break
    print(f"\nNombre: ", empleados[e]["nombre"])
    print(f"\nNumero de horas trabajadas:", empleados[e]["HorasT"])
    print(f"\nValor de la hora: $", empleados[e]["ValorH"])

def eliminar(empleados):
    id = leerInt("\nIngrese el id del empleado: ")
    for k in empleados.keys():
        if k == id:
            e = k
            break
    empleados.pop(e)    
    print("El empleado ha sido eliminado")

def listEmpleados(empleados):  
    while True:
        l = 0
        for k in empleados.keys():
            print(f"Id: {k}\tNombre: {empleados[k]['nombre']}\tHoras trabajadas: {empleados[k]['HorasT']}\tValor horas: {empleados[k]['ValorH']:,.0f}")
            l += 1
            if l >= (len(empleados)):
                return
            if l == 5:
                while True:
                    conf = int(input("\nSi desea continuar digite 1, si quiere salir presione 2: "))
                    if conf < 1 or conf > 2:
                        print("Ingrese una opción valida")
                        continue
                    break
                if conf == 2:
                    return

def nomEmpleado(empleados):
    auxi = 0
    id = leerInt("\nIngrese el id del empleado: ")
    for k in empleados.keys():
        if k == id:
            e = k
            break
    salBru = empleados[e]["HorasT"] * empleados[e]["ValorH"]
    if salBru < 1160000:
        auxi = 140606
    desPen = salBru * 0.04 
    desEPS = salBru * 0.04
    salNet = salBru + auxi - desPen - desEPS

    print(f"Id: {e}\tNombre: {empleados[e]['nombre']}\tHoras trabajadas: {empleados[e]['HorasT']}\tValor horas: {empleados[e]['ValorH']:,.0f}")
    print(f"Salario Bruto: {salBru:,.0f}\tAuxilio: {auxi:,.0f}\tDescuento pensión: -{desPen:,.0f}\tDescuento EPS: -{desEPS:,.0f}\tSalario neto: {salNet:,.0f}")

def nomEmpleados(empleados):
    while True:
        l = 0
        for k in empleados.keys():
                salBru = empleados[k]["HorasT"] * empleados[k]["ValorH"]
                if salBru < 1160000:
                    auxi = 140606
                desPen = salBru * 0.04 
                desEPS = salBru * 0.04
                salNet = salBru + auxi - desPen - desEPS
                print(f"Id: {k}\tNombre: {empleados[k]['nombre']}\tHoras trabajadas: {empleados[k]['HorasT']}\tValor horas: {empleados[k]['ValorH']:,.0f}")
                print(f"Salario Bruto: {salBru:,.0f}\tAuxilio: {auxi:,.0f}\tDescuento pensión: -{desPen:,.0f}\tDescuento EPS: -{desEPS:,.0f}\tSalario neto: {salNet:,.0f}")
                l += 1
                if l >= (len(empleados)):
                    return
                if l == 5:
                    while True:
                        conf = int(input("\nSi desea continuar digite 1, si quiere salir presione 2: "))
                        if conf < 1 or conf > 2:
                            print("Ingrese una opción valida")
                            continue
                        break
                    if conf == 2:
                        return

def salir():
    while True:
        des = leerInt("\nSi desea salir presione 1, si no desea salir presione 2: ")
        if des < 1 or des > 2:
            print("Por favor seleccione una de las dos opciones")
            continue
        return des

empleados = {}

while True:
    iOpc = menu()
    if iOpc == 1:
        id = leerInt("\nIngrese el numero de id: ")
        nom = leerString("Ingrese el nombre del empleado: ")
        while True:
            horasT = leerInt("Ingrese el numero de horas trabajadas del empleado: ")
            if horasT < 1 or horasT > 160:
                print("El numero de horas tiene que estar entre 1 y 160")
                continue
            break
        while True:
            valorH = leerInt("Ingrese el valor unitario de la hora: ")
            if valorH < 8000 or valorH > 150000:
                print("El valor de la horas tiene que estar entre 8.000 y 150.000")
                continue
            break   
        agregar(empleados, id, nom, horasT, valorH)
        print("_" * 75)
        print("\nLos datos fueron agregados")
        input("\nPresione cualquier tecla para continuar")
    elif iOpc == 2:
        modificar(empleados) 
        input("\nPresione cualquier tecla para continuar") 
    elif iOpc == 3:
        buscar(empleados)
        input("\nPresione cualquier tecla para continuar")
    elif iOpc == 4:
        eliminar(empleados)
        input("\nPresione cualquier tecla para continuar")
    elif iOpc == 5:
        listEmpleados(empleados)
        input("\nPresione cualquier tecla para continuar")
    elif iOpc == 6:
        nomEmpleado(empleados)
        input("\nPresione cualquier tecla para continuar")
    elif iOpc == 7:
        nomEmpleados(empleados)
        input("\nPresione cualquier tecla para continuar")        
    elif iOpc == 8:
        desi = salir()
        if desi == 1:
            print("\nFIN DEL PROGRAMA")
            break
        else:
            continue
