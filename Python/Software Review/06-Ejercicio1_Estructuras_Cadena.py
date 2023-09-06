while True:
    try:
        print("-" * 75)
        iNumUsu = int(input("Ingrese el numero de telefono con prefijo y extensión: "))
        break
    except ValueError:
        print("Ingrese un numero valido")
        continue

sNumUsu = str(iNumUsu)
sNumUsu_2 = sNumUsu[:-2]
sNumPrin = sNumUsu_2[2:]

print("-" * 75)
print(f"El numero ingresado eliminando el prefijo y la extensión es: {sNumPrin}\n"
      "Fin del programa")


            