print("Bienvenido programa para saber que numero es mayor o menos de 10 numeros diferentes (enteros positivos)")
iMen = 100000000000000
iMay = 0
for i in range(1, 11):
    iNum = int(input("Ingrese un numero: "))
    if iNum < iMen:
        iMen = iNum
    elif iNum > iMay:
        iMay = iNum
print(f"De los datos ingresados el numero mayor es: {iMay}")
print(f"de los datos ingresados el numero menor es: {iMen}")