iNum = int(input("Ingrese un numero entero positivo: "))
sCanDig = ""

if iNum < 10:
    sCanDig = "uno"
elif iNum < 100:
    sCanDig = "dos"
elif iNum < 1000:
    sCanDig = "tres"
elif iNum < 10000:
    sCanDig = "cuatro"
elif iNum < 100000:
    sCanDig = "cinco"
elif iNum < 1000000:
    sCanDig = "seis"
elif iNum < 10000000:
    sCanDig = "siete"
elif iNum < 100000000:
    sCanDig = "ocho"
elif iNum < 1000000000:
    sCanDig = "nueve"
elif iNum < 10000000000:
    sCanDig = "diez"
elif iNum > 10000000000:
    sCanDig = "mas de diez"
else:
    sCanDig = "no es un numero positivo"

print(f"El numero de digitos del numero {iNum} es {sCanDig}")