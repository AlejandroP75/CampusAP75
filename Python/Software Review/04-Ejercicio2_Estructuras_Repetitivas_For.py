iNum = int(input("Ingrese un numero entero: "))
fResu = 0

for i in range(1, iNum + 1):
    fResu = fResu + (((-1) ** (i+1)) * (1 / i))
    if ((-1) ** (i+1)) == 1:
        print(f"+(1 / {i})")
    else:
        print(f"-(1 / {i})")

print(f"El resultado de la serie es: {fResu}")    
    