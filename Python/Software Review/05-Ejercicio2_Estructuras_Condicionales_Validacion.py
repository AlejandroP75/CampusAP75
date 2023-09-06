prue = 0

while prue == 0:
    print("-" * 75)
    sOra = input("Ingresa una oración: ")
    sOraMay = sOra.upper()
    if sOraMay == "SALIR":
        print("Fin del programa")
        break
    sPalCla = input("Ingresa la palabra clave: ")
    sPalClaMay = sPalCla.upper()
    if sPalClaMay == "SALIR":
        print("-" * 75)
        print("Fin del programa")
        break
    
    if sPalClaMay in sOraMay:
        print("-" * 75)
        print("Felicidades la palabra clave esta en la oración")
        print("Fin del programa")
        break
    else: 
        print("Lo siento la palabra clave no esta en la oración, intentalo de nuevo o si quieres salir del programa escribe \"salir\"")
        continue
    
