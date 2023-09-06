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

def leerInt(msg):
    while True:
        try:
            print("_" * 70)
            iNum = int(input(msg))
            return iNum
        except ValueError:
            print("_" * 70)
            print("\nIngrese un numero entero valido")

def leerProgramaAcademico():
    print("_" * 70)
    print("\nProgramas academicos")
    print("\n1.Técnico en sistemas")
    print("\n2.Técnico en desarrolo de videojuegos")
    print("\n3.Técnico en animacion digital")
    iOpPro = leerInt("\nSeleccione el numero de su programa academico: ")
    while True:
        if iOpPro < 1 or iOpPro > 3:
            print("Por favor seleccione un opción valida, de 1 a 3")
            continue
        return iOpPro
    
def leerIndBeca():
    print("_" * 70)
    print("\nIndicadores de becas")
    print("\n1.Beca por rendimiento academico")
    print("\n2.Beca Cultura - Deportes")
    print("\n3.Sin beca")
    iOpPro = leerInt("\nSeleccion el numero de su indicador de beca: ")
    while True:
        if iOpPro < 1 or iOpPro > 3:
            print("Por favor seleccione un opción valida, de 1 a 3")
            continue
        return iOpPro

def calMatricula(iProgAcad, iBeca):
    if iProgAcad == 1:
        iValor = 800000
    elif iProgAcad == 2:
        iValor = 1000000
    else:
        iValor = 1200000
    
    if iBeca == 1:
        iDes = 0.5
        iValorNeto = iValor - (iValor * iDes)
    elif iBeca == 2:
        iDes = 0.4
        iValorNeto = iValor - (iValor * iDes)
    else:
        iValorNeto = iValor
    return iValorNeto

iCod = leerInt("\nIngrese el codigo del estudiante: ")
print("_" * 70)
sNom = leerString("\nIngrese el nombre del estudiante: ")
iProgAcad = leerProgramaAcademico()
iBeca = leerIndBeca()

iValNetoPagar = calMatricula(iProgAcad, iBeca)

print("_" * 70)
print(f"\nEstudiante: {sNom}"
      f"\n\nEl valor neto a pagar es: {iValNetoPagar:,.0f}")