# def nom_Funcion([param1, param2, ... ,param3 ]):
#     cuerpo_funcion

def sum (iNum1, iNum2):
    return iNum1 + iNum2

def leerInt(msg):
    while True:
        try:
            print("_" * 75)
            iNum = int(input(msg))
            return iNum
        except ValueError:
            print("_" * 75)
            print("Ingrese un numero entero valido")

iNum1 = leerInt("Ingrese el primer numero entero:")
iNum2 = leerInt("Ingrese el segundo numero entero: ")

print("_" * 75)
print(f"La suma de los numeros es {sum(iNum1, iNum2)}")
