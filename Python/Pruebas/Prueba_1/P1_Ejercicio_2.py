fLadA = float(input("Ingrese el lado a del triangulo: "))
fLadB = float(input("Ingrese el lado b del triangulo: "))
fLadC = float(input("Ingrese el lado c del triangulo: "))

fP = (fLadA + fLadB + fLadC) / 2
fArea = (fP * (fP - fLadA) * (fP - fLadB) * (fP - fLadC)) ** (1 / 2)

if (fP > fLadA) and (fP > fLadB) and (fP > fLadC):
    print(f"El area del triangulo es: {fArea:,.2f}")
else:
    print("Las medidas de los angulos ingresados no son las de un tringulo, por favor verifique")
