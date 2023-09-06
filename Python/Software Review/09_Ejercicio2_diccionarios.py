def leerInt(msg):
    while True:
        try:
            print("_" * 75)
            while True:
                iNum = int(input(msg))
                if iNum < 0:
                    print("El numero tiene que ser un numero positivo")
                    continue
                break
            return iNum
        except ValueError:
            print("_" * 75)
            print("Ingrese un numero entero valido")
            
while True:
    numIng = leerInt("Ingrese el numero de estudiantes suscritos al periodico en ingles: ")
    cod1= input("Ingrese el codgio de los estudiantes separados por espacio: ")
    codIng = cod1.split()
    codIng = [int(num) for num in codIng]
    print(codIng)
    if len(codIng) != numIng:
        print("El numero de estudiantes no coincide con el numero de codigos")
        continue
    break

while True:
    numFra = leerInt("Ingrese el numero de estudiantes suscritos al periodico en frances: ")
    cod2= input("Ingrese el codgio de los estudiantes separados por espacio: ")
    codFra = cod2.split()
    codFra = [int(num) for num in codFra]
    if len(codFra) != numFra:
        print("El numero de estudiantes no coincide con el numero de codigos")
        continue
    break

print(f"El numero de estudiantes suscritos unicamente al periodico en ingles es: {len(set(codIng) - set(codFra))}")

