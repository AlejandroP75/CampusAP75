#6.1

def leerInt(msg):
    while True:
        try:
            print("_" * 75)
            iNum = int(input(msg))
            return iNum
        except ValueError:
            print("_" * 75)
            print("Ingrese un numero entero valido")

def med(iN1, iN2, iN3):
    iMed = (iN1 + iN2 + iN3) / 3
    return iMed

iNum1 = leerInt("\nIngrese el primer numero: ")
iNum2 = leerInt("\nIngrese el segundo numero: ")
iNum3 = leerInt("\nIngrese el tercer numero: ")

iMedia = med(iNum1, iNum2, iNum3)

print("_" * 70)
print(f"\nLa media de los numeros {iNum1}, {iNum2} y {iNum3} es {iMedia:,.2f}")
