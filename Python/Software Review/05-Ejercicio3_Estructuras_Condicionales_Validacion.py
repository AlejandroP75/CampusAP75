iPrue = 0

while iPrue == 0:
    iCont = 0
    print("-" * 70)
    sFras = input("Ingrese una frase (si quiere salir ingrese la letra ""q""): ")
    sFrasMay = sFras.upper()

    for i in sFrasMay:
        if i.upper() in "AEIOU":
                iCont+= 1
    
    if sFrasMay == "Q":
        print("-" * 70)
        print("Fin del programa")
        break
    else:
        print(f"La frase /{sFras}/ tiene {iCont} vocales")